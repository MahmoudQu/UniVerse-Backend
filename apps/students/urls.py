from django.urls import path
from .views import signup_student, verify_otp_student, request_new_student_otp

urlpatterns = [
    path('signup/', signup_student, name='signup_student'),
    path('verify-otp/', verify_otp_student, name='verify_otp_student'),
    path('request-new-otp/', request_new_student_otp, name='request_new_student_otp'),
]
