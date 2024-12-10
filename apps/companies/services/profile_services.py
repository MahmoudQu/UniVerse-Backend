from apps.companies.models import Company
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404


def handle_company_profile_update(request):
    from apps.companies.serializers import CompanySerializer

    company = get_object_or_404(Company, user=request.user)
    serializer = CompanySerializer(company, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response({"message": "Your profile updated successfully."}, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)