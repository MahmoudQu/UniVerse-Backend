from django.utils import timezone
from apps.accounts.models import RefreshToken
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authtoken.models import Token


def generate_refresh_token(user):
    refresh_token, created = RefreshToken.objects.get_or_create(user=user)
    if not created:
        refresh_token.key = refresh_token.generate_key()
        refresh_token.expiration = timezone.now() + timezone.timedelta(days=7)
        refresh_token.save()
    return refresh_token.key


def refresh_user_token(request):
    refresh_token_key = request.data.get('refresh_token')

    try:
        token_obj = RefreshToken.objects.get(
            key=refresh_token_key,
            expiration__gt=timezone.now()
        )
        user = token_obj.user
        token, _ = Token.objects.get_or_create(user=user)
        new_refresh_token = generate_refresh_token(user)
        return Response({
            'token': token.key,
            'refresh_token': new_refresh_token,
        }, status=status.HTTP_200_OK)
    except RefreshToken.DoesNotExist:
        return Response({"detail": "Invalid or expired refresh token."}, status=status.HTTP_400_BAD_REQUEST)
