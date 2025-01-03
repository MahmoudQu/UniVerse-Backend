from django.shortcuts import render
from rest_framework import generics, permissions
from .models import Education
from .serializers import EducationSerializer
from permissions import student_permission


class EducationListCreateView(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Education.objects.all()
    serializer_class = EducationSerializer


class EducationDetailView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Education.objects.all()
    serializer_class = EducationSerializer
