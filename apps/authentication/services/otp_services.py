import uuid
from django.utils import timezone
from rest_framework.response import Response
from rest_framework import status
from utils.sendEmailToUser import send_email_to_user


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
    send_email_to_user(user.email, "OTP Verification", f"Please verify your email with this OTP: {user.otp}")
    return Response({"message": "A new OTP has been sent to your email."}, status=status.HTTP_200_OK)