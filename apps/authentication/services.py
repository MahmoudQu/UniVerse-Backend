import uuid
from django.core.mail import send_mail
from django.contrib.auth import authenticate
from django.utils import timezone
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework import status
from apps.accounts.models import RefreshToken


def authenticate_user(email, password):
    user = authenticate(email=email, password=password)
    if user:
        token, _ = Token.objects.get_or_create(user=user)
        return user, token.key
    return None, None


def send_otp_email(user_email, otp):
    send_mail(
        'Your OTP Code',
        f'Your OTP code is {otp}',
        'jouniversejo@gmail.com',
        [user_email],
        fail_silently=False,
    )


def verify_otp(user, otp):
    if user.otp == otp and user.otp_expiration > timezone.now():
        user.is_verified = True
        user.save()
        return True
    return False


def request_new_otp(user):
    profile = None
    if hasattr(user, 'student'):
        profile = user.student
    elif hasattr(user, 'company'):
        profile = user.company
    else:
        return Response({"detail": "User profile not found."}, status=status.HTTP_400_BAD_REQUEST)

    if profile.is_verified:
        return Response({"detail": "Email is already verified."}, status=status.HTTP_400_BAD_REQUEST)

    # Generate a new OTP
    user.otp = str(uuid.uuid4().int)[:6]
    user.otp_expiration = timezone.now() + timezone.timedelta(minutes=10)
    user.save()

    # Send the OTP
    send_otp_email(user.email, user.otp)
    return Response({"message": "A new OTP has been sent to your email."}, status=status.HTTP_200_OK)


def generate_refresh_token(user):
    """
    Generate or update a refresh token for the user.
    """
    refresh_token, created = RefreshToken.objects.get_or_create(user=user)
    if not created:
        refresh_token.key = refresh_token.generate_key()
        refresh_token.expiration = timezone.now() + timezone.timedelta(days=7)
        refresh_token.save()
    return refresh_token.key
