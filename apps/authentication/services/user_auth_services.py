from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from .token_services import generate_refresh_token
from rest_framework.response import Response
from rest_framework import status
from apps.accounts.models import RefreshToken
from apps.accounts.serializers import UserSerializer


def authenticate_user(email, password):
    user = authenticate(email=email, password=password)
    if user:
        token, _ = Token.objects.get_or_create(user=user)
        return user, token.key
    return None, None


def handle_login(request):
    email = request.data.get('email')
    password = request.data.get('password')

    if not email or not password:
        return Response(
            {"detail": "Email and password are required."},
            status=status.HTTP_400_BAD_REQUEST,
        )

    user, token = authenticate_user(email, password)

    if user is not None:
        user.is_logged_in = True
        user.save(update_fields=['is_logged_in'])
        user_type = 'student' if hasattr(user, 'student') else 'company' if hasattr(
            user, 'company') else 'unknown'
        refresh_token = generate_refresh_token(user)
        serializer = UserSerializer(user, context={'request': request})
        return Response(
            {
                "token": token,
                "refresh_token": refresh_token,
                "user_type": user_type,
                "is_logged_in": user.is_logged_in,
                "user": serializer.data
            },
            status=status.HTTP_200_OK,
        )
    return Response(
        {"detail": "Invalid email or password."},
        status=status.HTTP_401_UNAUTHORIZED,
    )


def handle_logout(request):
    user = request.user
    user.is_logged_in = False
    user.save(update_fields=['is_logged_in'])
    Token.objects.filter(user=user).delete()
    RefreshToken.objects.filter(user=user).delete()

    return Response({"detail": "Logged out successfully."}, status=status.HTTP_200_OK)


def check_user_verification(request):
    user = request.user
    if hasattr(user, 'student'):
        is_verified = user.student.is_verified
    elif hasattr(user, 'company'):
        is_verified = user.company.is_verified
    else:
        return Response({"detail": "User profile not found."}, status=status.HTTP_404_NOT_FOUND)

    return Response({"is_verified": is_verified}, status=status.HTTP_200_OK)
