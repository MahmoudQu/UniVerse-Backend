# apps/authentication/urls.py

from django.urls import path
from . import views
from .views import login, check_user_verification

urlpatterns = [
    path('student/signup/', views.student_signup, name='student_signup'),
    path('student/verify_otp/', views.student_verify_otp,
         name='student_verify_otp'),
    path('student/request_new_otp/', views.student_request_new_otp,
         name='student_request_new_otp'),
    path('company/signup/', views.company_signup, name='company_signup'),
    path('company/verify_otp/', views.company_verify_otp,
         name='company_verify_otp'),
    path('company/request_new_otp/', views.company_request_new_otp,
         name='company_request_new_otp'),
    path('login/', login, name='login'),
    path('refresh_token/', views.refresh_token, name='refresh_token'),
    path('api_call_success/', views.api_call_success, name='api_call_success'),
    path('check_verification/', check_user_verification, name='check_verification'),
    path('logout/', views.logout, name='logout'),
    path('user_data/', views.get_user_data, name='get_user_data'),
]
