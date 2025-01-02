from rest_framework import permissions
from rest_framework.views import APIView
from .services.main import *
from .services.token_services import refresh_user_token


class UpdatePasswordView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def put(self, request):
        return update_user_password(request)


class UpdateEmailView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def put(self, request):
        return update_user_email(request)


class UpdateImageView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def put(self, request, *args, **kwargs):
        return update_user_image(request)


class GetProfileView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, *args, **kwargs):
        return get_profile(request)


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
