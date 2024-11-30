from rest_framework_simplejwt.tokens import AccessToken
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.exceptions import TokenError, InvalidToken


def generate_refresh_token(user):
    refresh = RefreshToken.for_user(user)
    return str(refresh)


def refresh_user_token(request):
    refresh_token = request.data.get('refresh_token')
    try:
        refresh = RefreshToken(refresh_token)
        new_access_token = refresh.access_token
        return Response({
            'access_token': str(new_access_token),
            'refresh_token': str(refresh),
        }, status=status.HTTP_200_OK)
    except TokenError:
        return Response(
            {"detail": "Invalid or expired refresh token."},
            status=status.HTTP_400_BAD_REQUEST
        )


def validate_user_token(request):
    auth_header = request.META.get('HTTP_AUTHORIZATION', None)
    if not auth_header:
        return Response({"detail": "Authorization header missing."}, status=status.HTTP_400_BAD_REQUEST)
    try:
        token_type, token_string = auth_header.split(' ')
        assert token_type == 'Bearer'
    except (ValueError, AssertionError):
        return Response({"detail": "Invalid authorization header format."}, status=status.HTTP_400_BAD_REQUEST)
    try:
        access_token = AccessToken(token_string)
        user_id = access_token['user_id']
        # Optionally, you can verify if the user exists in your system
        return Response({"detail": "Token is valid.", "user_id": user_id}, status=status.HTTP_200_OK)
    except (TokenError, InvalidToken):
        return Response({"detail": "Invalid or expired token."}, status=status.HTTP_401_UNAUTHORIZED)
