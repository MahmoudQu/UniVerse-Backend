# apps/students/views.py

from rest_framework import generics, permissions
from .serializers import StudentSerializer
from apps.authentication.services.main import (
    handle_student_signup,
    handle_student_otp_verification,
    handle_student_new_otp,
)


class StudentSignupView(generics.CreateAPIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = StudentSerializer

    def create(self, request, *args, **kwargs):
        return handle_student_signup(request)


class StudentVerifyOTPView(generics.CreateAPIView):
    permission_classes = [permissions.AllowAny]

    def create(self, request, *args, **kwargs):
        return handle_student_otp_verification(request)


class StudentRequestNewOTPView(generics.CreateAPIView):
    permission_classes = [permissions.AllowAny]

    def create(self, request, *args, **kwargs):
        return handle_student_new_otp(request)