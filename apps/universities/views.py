from django.shortcuts import render
from rest_framework import generics
from .models import University, Major
from .serializers import UniversitySerializer, MajorSerializer


class UniversityListCreateView(generics.ListCreateAPIView):
    queryset = University.objects.all()
    serializer_class = UniversitySerializer


class UniversityDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = University.objects.all()
    serializer_class = UniversitySerializer


class MajorListCreateView(generics.ListCreateAPIView):
    queryset = Major.objects.all()
    serializer_class = MajorSerializer


class MajorDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Major.objects.all()
    serializer_class = MajorSerializer

class MajorsByUniversityView(generics.ListAPIView):
    serializer_class = MajorSerializer
    
    def get_queryset(self):
        university_id = self.kwargs['university_id']
        return Major.objects.filter(university_id=university_id)
