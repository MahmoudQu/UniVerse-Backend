from django.urls import path
from .views import signup_company, verify_otp_company, request_new_company_otp

urlpatterns = [
    path('signup/', signup_company, name='signup_company'),
    path('verify-otp/', verify_otp_company, name='verify_otp_company'),
    path('request-new-otp/', request_new_company_otp, name='request_new_company_otp'),
]