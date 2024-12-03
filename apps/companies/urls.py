# apps/companies/urls.py
from django.urls import path
from .views import (
    CompanySignupView,
    CompanyVerifyOTPView,
    CompanyRequestNewOTPView,
)

urlpatterns = [
    path('signup/', CompanySignupView.as_view(), name='company_signup'),
    path('verify_otp/', CompanyVerifyOTPView.as_view(), name='company_verify_otp'),
    path('request_new_otp/', CompanyRequestNewOTPView.as_view(), name='company_request_new_otp'),
]