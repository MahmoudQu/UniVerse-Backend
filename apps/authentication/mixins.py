from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from apps.accounts.models import CustomUser
from apps.accounts.serializers import UserSerializer
from .services import send_otp_email, verify_otp, request_new_otp, authenticate_user, generate_refresh_token
from django.utils import timezone
from rest_framework.authtoken.models import Token
from apps.accounts.models import RefreshToken
from rest_framework.permissions import IsAuthenticated


class GetUserDataMixin:
    def get_user_data(self, request):
        user = request.user
        if user.is_authenticated:
            token = request.auth.key if hasattr(request.auth, 'key') else None

            # Set is_logged_in to True
            user.is_logged_in = True
            user.save(update_fields=['is_logged_in'])

            # Determine the user_type based on related profiles
            if hasattr(user, 'student'):
                user_type = 'student'
            elif hasattr(user, 'company'):
                user_type = 'company'
            else:
                user_type = 'unknown'

            # Generate a refresh token
            refresh_token = generate_refresh_token(user)

            # Serialize the user data
            serializer = UserSerializer(user, context={'request': request})

            return Response(
                {
                    "token": token,
                    "refresh_token": refresh_token,
                    "user_type": user_type,
                    "is_logged_in": user.is_logged_in,
                    "user": serializer.data
                },
                status=status.HTTP_200_OK
            )
        else:
            return Response(
                {"detail": "Authentication credentials were not provided."},
                status=status.HTTP_401_UNAUTHORIZED
            )


class SignupMixin:
    def signup_user(self, serializer, ProfileModel, email_field='email'):
        if serializer.is_valid():
            email = serializer.validated_data[email_field]
            if CustomUser.objects.filter(email=email).exists():
                return Response({"detail": "Email already exists."}, status=status.HTTP_400_BAD_REQUEST)
            profile = serializer.save()
            user = profile.user
            user.generate_otp()
            user.save()
            send_otp_email(user.email, user.otp)
            return Response({"message": "OTP generated. Please verify."}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LoginMixin:
    def login_user(self, request):
        email = request.data.get('email')
        password = request.data.get('password')

        if not email or not password:
            return Response(
                {"detail": "Email and password are required."},
                status=status.HTTP_400_BAD_REQUEST
            )

        user, token = authenticate_user(email, password)

        if user is not None:
            # Set is_logged_in to True
            user.is_logged_in = True
            user.save(update_fields=['is_logged_in'])

            # Determine the user_type based on related profiles
            if hasattr(user, 'student'):
                user_type = 'student'
            elif hasattr(user, 'company'):
                user_type = 'company'
            else:
                user_type = 'unknown'

            # Generate a refresh token
            refresh_token = generate_refresh_token(user)

            # Serialize the user data
            serializer = UserSerializer(user, context={'request': request})

            return Response(
                {
                    "token": token,
                    "refresh_token": refresh_token,
                    "user_type": user_type,
                    "is_logged_in": user.is_logged_in,
                    "user": serializer.data
                },
                status=status.HTTP_200_OK
            )
        else:
            return Response(
                {"detail": "Invalid email or password."},
                status=status.HTTP_401_UNAUTHORIZED
            )


class LogoutMixin:
    permission_classes = [IsAuthenticated]

    def logout_user(self, request):
        user = request.user
        if user.is_authenticated:
            # Set is_logged_in to False
            user.is_logged_in = False
            user.save(update_fields=['is_logged_in'])

            # Delete the user's auth token and refresh token
            Token.objects.filter(user=user).delete()
            RefreshToken.objects.filter(user=user).delete()

            return Response({"detail": "Logged out successfully."}, status=status.HTTP_200_OK)
        else:
            return Response({"detail": "User is not authenticated."}, status=status.HTTP_400_BAD_REQUEST)


class OTPMixin:
    def verify_otp(self, request, ProfileModel):
        email = request.data.get('email')
        otp = request.data.get('otp')
        user = get_object_or_404(CustomUser, email=email)
        profile = get_object_or_404(ProfileModel, user=user)
        if verify_otp(user, otp):
            profile.is_verified = True
            profile.save()
            return Response({"message": "Email verified successfully."}, status=status.HTTP_200_OK)
        return Response({"detail": "Invalid or expired OTP."}, status=status.HTTP_400_BAD_REQUEST)

    def request_new_otp(self, request, ProfileModel):
        email = request.data.get('email')
        user = get_object_or_404(CustomUser, email=email)
        profile = get_object_or_404(ProfileModel, user=user)
        return request_new_otp(user)


class RefreshTokenMixin:
    def refresh_access_token(self, request):
        refresh_token_key = request.data.get('refresh_token')

        try:
            token_obj = RefreshToken.objects.get(
                key=refresh_token_key,
                expiration__gt=timezone.now()
            )
            user = token_obj.user
            # Generate new access token
            token, _ = Token.objects.get_or_create(user=user)
            # Optionally, refresh the refresh token as well
            new_refresh_token = generate_refresh_token(user)
            serializer = UserSerializer(user, context={'request': request})
            return Response({
                'user': serializer.data,
                'token': token.key,
                'refresh_token': new_refresh_token
            }, status=status.HTTP_200_OK)
        except RefreshToken.DoesNotExist:
            return Response({"detail": "Invalid or expired refresh token."},
                            status=status.HTTP_400_BAD_REQUEST)


class VerificationMixin:
    def check_user_verification(self, request):
        user = request.user

        # Check if the user has a Student profile
        if hasattr(user, 'student'):
            is_verified = user.student.is_verified
        # Check if the user has a Company profile
        elif hasattr(user, 'company'):
            is_verified = user.company.is_verified
        else:
            # User does not have a profile with is_verified attribute
            return Response(
                {"detail": "User profile not found."},
                status=status.HTTP_404_NOT_FOUND
            )

        return Response(
            {"is_verified": is_verified},
            status=status.HTTP_200_OK
        )
