from django.urls import path
from .views import (
    StudentSignupView,
    CompanySignupView,
    StudentVerifyOTPView,
    CompanyVerifyOTPView,
    StudentRequestNewOTPView,
    CompanyRequestNewOTPView,
    LoginView,
    LogoutView,
    RefreshTokenView,
    CheckVerificationView,
    GetUserDataView
)

urlpatterns = [
    path('student/signup/', StudentSignupView.as_view(), name='student_signup'),
    path('company/signup/', CompanySignupView.as_view(), name='company_signup'),
    path('student/verify_otp/', StudentVerifyOTPView.as_view(),
         name='student_verify_otp'),
    path('company/verify_otp/', CompanyVerifyOTPView.as_view(),
         name='company_verify_otp'),
    path('student/request_new_otp/', StudentRequestNewOTPView.as_view(),
         name='student_request_new_otp'),
    path('company/request_new_otp/', CompanyRequestNewOTPView.as_view(),
         name='company_request_new_otp'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('refresh_token/', RefreshTokenView.as_view(), name='refresh_token'),
    path('check_verification/', CheckVerificationView.as_view(),
         name='check_verification'),
    path('user_data/', GetUserDataView.as_view(),
         name='user_data')
]
