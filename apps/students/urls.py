# apps/students/urls.py
from django.urls import path
from .views import (
    StudentListCreateView,
    StudentDetailView,
    StudentSignupView,
    StudentVerifyOTPView,
    StudentRequestNewOTPView,
    StudentUpdateProfileView,
    FeaturedStudentsView,
    StudentResumeInfoView,
    StudentSearchView
)

urlpatterns = [
    path('students/', StudentListCreateView.as_view(), name='student_list'),
    path('students/<int:pk>/', StudentDetailView.as_view(), name='student_detail'),
    path('students/signup/', StudentSignupView.as_view(), name='student_signup'),
    path('students/verify_otp/', StudentVerifyOTPView.as_view(),
         name='student-verify-otp'),
    path('students/request_new_otp/', StudentRequestNewOTPView.as_view(),
         name='student-request-new-otp'),
    path('student/update_profile/', StudentUpdateProfileView.as_view(),
         name='student_update_profile'),
    path('students/featured_students/', FeaturedStudentsView.as_view(),
         name='featured_students'),
    path('students/<int:id>/resume_info/',
         StudentResumeInfoView.as_view(), name='student_resume_info'),
    path('students/search/', StudentSearchView.as_view(), name='student_search'),
]
