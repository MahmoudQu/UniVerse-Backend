from apps.accounts.models import CustomUser
from apps.students.models import Student
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from utils.sendEmailToUser import send_email_to_user
from .otp_services import verify_otp, request_new_otp


def handle_student_signup(request):
    from apps.students.serializers import StudentSerializer

    serializer = StudentSerializer(data=request.data)
    if serializer.is_valid():
        email = serializer.validated_data['email']
        if CustomUser.objects.filter(email=email).exists():
            return Response({"detail": "Email already exists."}, status=status.HTTP_400_BAD_REQUEST)
        profile = serializer.save()
        user = profile.user
        user.generate_otp()
        user.save()
        send_email_to_user(user.email, "OTP Verification",
                           f"Please verify your email with this OTP: {user.otp}")
        return Response({"message": "OTP generated. Please verify."}, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


def handle_student_otp_verification(request):
    email = request.data.get('email')
    otp = request.data.get('otp')
    user = get_object_or_404(CustomUser, email=email)
    profile = get_object_or_404(Student, user=user)
    if verify_otp(user, otp):
        profile.is_verified = True
        profile.save()
        return Response({"message": "Email verified successfully."}, status=status.HTTP_200_OK)
    return Response({"detail": "Invalid or expired OTP."}, status=status.HTTP_400_BAD_REQUEST)


def handle_student_new_otp(request):
    email = request.data.get('email')
    user = get_object_or_404(CustomUser, email=email)
    profile = get_object_or_404(Student, user=user)
    return request_new_otp(user)
