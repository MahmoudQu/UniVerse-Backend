from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView
from apps.accounts.models import RefreshToken
from apps.students.serializers import StudentSerializer
from apps.companies.serializers import CompanySerializer
from .services.main import *
from .services.token_services import refresh_user_token
from rest_framework.authtoken.models import Token


class StudentSignupView(generics.CreateAPIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = StudentSerializer

    def post(self, request, *args, **kwargs):
        return handle_student_signup(request)


class CompanySignupView(generics.CreateAPIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = CompanySerializer

    def post(self, request, *args, **kwargs):
        return handle_company_signup(request)


class StudentVerifyOTPView(APIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request, *args, **kwargs):
        return handle_student_otp_verification(request)


class CompanyVerifyOTPView(APIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request, *args, **kwargs):
        return handle_company_otp_verification(request)


class StudentRequestNewOTPView(APIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request, *args, **kwargs):
        return handle_student_new_otp(request)


class CompanyRequestNewOTPView(APIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request, *args, **kwargs):
        return handle_company_new_otp(request)


class LoginView(APIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request, *args, **kwargs):
        return handle_login(request)


class LogoutView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, *args, **kwargs):
        return handle_logout(request)


class RefreshTokenView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, *args, **kwargs):
        return refresh_user_token(request)


class CheckVerificationView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, *args, **kwargs):
        return check_user_verification(request)


class GetUserDataView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, *args, **kwargs):
        return get_user_data(request)
