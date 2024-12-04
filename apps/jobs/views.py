from django.shortcuts import render
# Create your views here.
from rest_framework import generics, permissions
from .models import JobPost, Application, SavedJob
from .serializers import JobPostSerializer, ApplicationSerializer, SavedJobSerializer

class JobPostListCreateView(generics.ListCreateAPIView):
    permission_classes=[permissions.AllowAny]
    queryset = JobPost.objects.all()
    serializer_class = JobPostSerializer


class JobPostDetailView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes=[permissions.AllowAny]
    queryset = JobPost.objects.all()
    serializer_class = JobPostSerializer


class ApplicationListCreateView(generics.ListCreateAPIView):
    permission_classes=[permissions.AllowAny]
    queryset = Application.objects.all()
    serializer_class = ApplicationSerializer


class ApplicationDetailView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes=[permissions.AllowAny]
    queryset = Application.objects.all()
    serializer_class = ApplicationSerializer


class SavedJobListCreateView(generics.ListCreateAPIView):
    permission_classes=[permissions.AllowAny]
    queryset = SavedJob.objects.all()
    serializer_class = SavedJobSerializer


class SavedJobDetailView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes=[permissions.AllowAny]
    queryset = SavedJob.objects.all()
    serializer_class = SavedJobSerializer

