# apps/students/urls.py
from django.urls import path
from .views import (
    StudentSignupView,
    StudentVerifyOTPView,
    StudentRequestNewOTPView,
)

urlpatterns = [
    path('signup/', StudentSignupView.as_view(), name='student_signup'),
    path('verify_otp/', StudentVerifyOTPView.as_view(), name='student_verify_otp'),
    path('request_new_otp/', StudentRequestNewOTPView.as_view(),
         name='student_request_new_otp'),
]
