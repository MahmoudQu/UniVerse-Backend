# apps/companies/views.py

from rest_framework import generics, permissions
from .serializers import CompanySerializer
from .models import Company
from apps.authentication.services.main import (
    handle_company_signup,
    handle_company_otp_verification,
    handle_company_new_otp,
)


class CompanyListCreateView(generics.ListCreateAPIView):
    permission_classes = [permissions.AllowAny]
    queryset = Company.objects.all()
    serializer_class = CompanySerializer


class CompanyDetailView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.AllowAny]
    queryset = Company.objects.all()
    serializer_class = CompanySerializer


class CompanySignupView(generics.CreateAPIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = CompanySerializer

    def create(self, request, *args, **kwargs):
        return handle_company_signup(request)


class CompanyVerifyOTPView(generics.CreateAPIView):
    permission_classes = [permissions.AllowAny]

    def create(self, request, *args, **kwargs):
        return handle_company_otp_verification(request)


class CompanyRequestNewOTPView(generics.CreateAPIView):
    permission_classes = [permissions.AllowAny]

    def create(self, request, *args, **kwargs):
        return handle_company_new_otp(request)
