from django.contrib.auth import authenticate
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from apps.accounts.serializers import UserSerializer
from rest_framework_simplejwt.token_blacklist.models import BlacklistedToken
from django.contrib.auth import get_user_model


def authenticate_user(email, password):
    user = authenticate(email=email, password=password)
    if user:
        refresh = RefreshToken.for_user(user)
        access_token = str(refresh.access_token)
        refresh_token = str(refresh)
        return user, access_token, refresh_token
    return None, None, None


def handle_login(request):
    email = request.data.get('email')
    password = request.data.get('password')
    user, access_token, refresh_token = authenticate_user(email, password)
    if user:
        user.is_logged_in = True
        user.save(update_fields=['is_logged_in'])
        return Response(
            {
                'user': UserSerializer(user).data,
                'access_token': access_token,
                'refresh_token': refresh_token,
                "is_logged_in": user.is_logged_in,
            },
            status=status.HTTP_200_OK
        )
    else:
        return Response(
            {"detail": "Invalid credentials."},
            status=status.HTTP_400_BAD_REQUEST
        )


def handle_logout(request):
    try:
        refresh_token = request.data.get("refresh")
        token = RefreshToken(refresh_token)

        # Check if the token is already blacklisted
        if BlacklistedToken.objects.filter(token__jti=token['jti']).exists():
            return Response({"detail": "Token has already been blacklisted."}, status=status.HTTP_400_BAD_REQUEST)

        # Blacklist the refresh token
        token.blacklist()

        # Retrieve the user and update the is_logged_in field
        user_id = token['user_id']
        User = get_user_model()
        user = User.objects.get(id=user_id)
        user.is_logged_in = False
        user.save(update_fields=['is_logged_in'])

        return Response({"detail": "Logout successful."}, status=status.HTTP_205_RESET_CONTENT)
    except Exception as e:
        return Response({"detail": "Logout failed."}, status=status.HTTP_400_BAD_REQUEST)


def check_user_verification(request):
    user = request.user
    user_type = 'student' if hasattr(user, 'student') else 'company' if hasattr(
        user, 'company') else 'unknown'
    email = user.email
    is_logged_in = user.is_logged_in
    if hasattr(user, 'student'):
        is_verified = user.student.is_verified
    elif hasattr(user, 'company'):
        is_verified = user.company.is_verified
    else:
        return Response({"detail": "Invalid user type."}, status=status.HTTP_404_NOT_FOUND)

    return Response({"is_verified": is_verified, "is_logged_in": is_logged_in, "user_type": user_type, "email": email}, status=status.HTTP_200_OK)
