# apps/companies/urls.py
from django.urls import path
from .views import (
    CompanyListCreateView,
    CompanyDetailView,
    CompanySignupView,
    CompanyVerifyOTPView,
    CompanyRequestNewOTPView,
    CompanyProfileUpdateView,
    FeaturedCompaniesView
)

urlpatterns = [
    path('companies/', CompanyListCreateView.as_view(), name='company_list'),
    path('companies/<int:pk>/', CompanyDetailView.as_view(), name='company_detail'),
    path('companies/signup/', CompanySignupView.as_view(), name='company_signup'),
    path('companies/verify_otp/', CompanyVerifyOTPView.as_view(),
         name='company_verify_otp'),
    path('companies/request_new_otp/', CompanyRequestNewOTPView.as_view(),
         name='company_request_new-otp'),
    path('company/update_profile/', CompanyProfileUpdateView.as_view(),
         name='company_update_profile'),
    path('companies/featured_companies/',
         FeaturedCompaniesView.as_view(), name='featured_companies'),
]
