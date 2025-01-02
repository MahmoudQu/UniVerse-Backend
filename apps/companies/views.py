# apps/companies/views.py

from rest_framework import generics, permissions
from rest_framework.views import APIView

from apps.jobs.models import JobPost
from .serializers import CompanySerializer
from .models import Company
from apps.authentication.services.main import (
    handle_company_signup,
    handle_company_otp_verification,
    handle_company_new_otp,
)
from .services.profile_services import handle_company_profile_update
from rest_framework.response import Response
from random import sample


class FeaturedCompaniesView(generics.ListAPIView):
    def get(self, request):
        companies = Company.objects.all()
        random_companies = sample(list(companies), min(12, len(companies)))
        data = []
        for company in random_companies:
            job_posts = JobPost.objects.filter(
                company=company, status=True).count()
            data.append({
                'id': company.id,
                'image': company.image,
                'name': company.name,
                'country': company.country,
                'city': company.city,
                'job_posts': job_posts
            })
        return Response(data)


class CompanyListCreateView(generics.ListCreateAPIView):
    permission_classes = [permissions.AllowAny]
    queryset = Company.objects.all()
    serializer_class = CompanySerializer


class CompanyDetailView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.AllowAny]
    queryset = Company.objects.all()
    serializer_class = CompanySerializer

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        data = serializer.data

        # Get 3 random active job posts from this company
        random_jobs = JobPost.objects.filter(
            company=instance,
            status=True
        ).order_by('?')[:3].values(
            'id', 'title', 'description', 'type',
            'salary_range', 'created_at'
        )

        # Add user and jobs data to response
        response_data = {
            **data,
            'user': {
                'email': instance.user.email,
            },
            'random_jobs': list(random_jobs)
        }

        return Response(response_data)


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


class CompanyProfileUpdateView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def put(self, request, *args, **kwargs):
        return handle_company_profile_update(request)
