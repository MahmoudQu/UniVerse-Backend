from django.shortcuts import render
from rest_framework import generics, permissions
from .models import Education
from .serializers import EducationSerializer

class EducationListCreateView(generics.ListCreateAPIView):
    permission_classes = [permissions.AllowAny]
    queryset = Education.objects.all()
    serializer_class = EducationSerializer


class EducationDetailView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.AllowAny]
    queryset = Education.objects.all()
    serializer_class = EducationSerializer
