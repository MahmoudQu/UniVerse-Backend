from rest_framework import permissions, status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate
from .models import Admin
from apps.accounts.models import CustomUser

class AdminLoginView(APIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        email = request.data.get('email')
        password = request.data.get('password')

        user = authenticate(email=email, password=password)
        
        if user and hasattr(user, 'admin'):
            refresh = RefreshToken.for_user(user)
            admin = user.admin

            return Response({
                'access_token': str(refresh.access_token),
                'refresh_token': str(refresh),
                'admin': {
                    'id': admin.id,
                    'email': user.email,
                    'first_name': admin.first_name,
                    'last_name': admin.last_name
                }
            }, status=status.HTTP_200_OK)
        
        return Response(
            {"detail": "Invalid credentials."},
            status=status.HTTP_401_UNAUTHORIZED
        )

class AdminLogoutView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        try:
            refresh_token = request.data.get('refresh')
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response(
                {"detail": "Successfully logged out."},
                status=status.HTTP_200_OK
            )
        except Exception:
            return Response(
                {"detail": "Invalid token."},
                status=status.HTTP_400_BAD_REQUEST
            )