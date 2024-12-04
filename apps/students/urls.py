# apps/students/urls.py
from django.urls import path
from .views import (
    StudentListCreateView,
    StudentDetailView,
    StudentSignupView,
    StudentVerifyOTPView,
    StudentRequestNewOTPView,
)

urlpatterns = [
    path('students/', StudentListCreateView.as_view(), name='student_list'),
    path('students/<int:pk>/', StudentDetailView.as_view(), name='student_detail'),
    path('students/signup/', StudentSignupView.as_view(), name='student_signup'),
    path('students/verify_otp/', StudentVerifyOTPView.as_view(),
         name='student-verify-otp'),
    path('students/request_new_otp/', StudentRequestNewOTPView.as_view(),
         name='student-request-new-otp'),
]
