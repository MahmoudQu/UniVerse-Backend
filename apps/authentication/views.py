from rest_framework import generics, permissions
from rest_framework.views import APIView
from .services.main import *
from .services.token_services import refresh_user_token


class LoginView(APIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request, *args, **kwargs):
        return handle_login(request)


class LogoutView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, *args, **kwargs):
        return handle_logout(request)


class RefreshTokenView(APIView):
    permission_classes = [permissions.AllowAny]

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


class CheckTokenView(APIView):
    permission_classes = [permissions.AllowAny]

    def get(self, request, *args, **kwargs):
        return validate_user_token(request)
