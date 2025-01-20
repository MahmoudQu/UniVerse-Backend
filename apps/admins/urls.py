# apps/admins/urls.py
from django.urls import path
from .views import AdminLoginView, AdminLogoutView

urlpatterns = [
    path('admins/login/', AdminLoginView.as_view(), name='admin_login'),
    path('admins/logout/', AdminLogoutView.as_view(), name='admin_logout'),
]