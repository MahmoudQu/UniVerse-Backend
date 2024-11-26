

# Create your views here.
from rest_framework.decorators import api_view, permission_classes
from .mixins import SignupMixin, OTPMixin, LoginMixin, VerificationMixin, LogoutMixin, RefreshTokenMixin, GetUserDataMixin
from apps.students.models import Student
from apps.companies.models import Company
from apps.students.serializers import StudentSerializer
from apps.companies.serializers import CompanySerializer
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework import status


signup_mixin = SignupMixin()
otp_mixin = OTPMixin()
login_mixin = LoginMixin()
logout_mixin = LogoutMixin()
refresh_token_mixin = RefreshTokenMixin()
verification_mixin = VerificationMixin()
get_user_data_mixin = GetUserDataMixin()


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_user_data(request):
    return get_user_data_mixin.get_user_data(request)


@api_view(['POST'])
@permission_classes([AllowAny])
def login(request):
    return login_mixin.login_user(request)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def logout(request):
    return logout_mixin.logout_user(request)


@api_view(['POST'])
@permission_classes([AllowAny])
def student_signup(request):
    serializer = StudentSerializer(data=request.data)
    return signup_mixin.signup_user(serializer, Student)


@api_view(['POST'])
@permission_classes([AllowAny])
def student_verify_otp(request):
    return otp_mixin.verify_otp(request, Student)


@api_view(['POST'])
@permission_classes([AllowAny])
def student_request_new_otp(request):
    return otp_mixin.request_new_otp(request, Student)


@api_view(['POST'])
@permission_classes([AllowAny])
def company_signup(request):
    serializer = CompanySerializer(data=request.data)
    return signup_mixin.signup_user(serializer, Company)


@api_view(['POST'])
@permission_classes([AllowAny])
def company_verify_otp(request):
    return otp_mixin.verify_otp(request, Company)


@api_view(['POST'])
@permission_classes([AllowAny])
def company_request_new_otp(request):
    return otp_mixin.request_new_otp(request, Company)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def refresh_token(request):
    return refresh_token_mixin.refresh_access_token(request)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def check_user_verification(request):
    return verification_mixin.check_user_verification(request)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def api_call_success(request):
    return Response({'data': 'API call success'}, status=status.HTTP_200_OK)
