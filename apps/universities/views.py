from rest_framework import generics, permissions
from .models import University
from .serializers import UniversitySerializer

class UniversityListCreateView(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = University.objects.all()
    serializer_class = UniversitySerializer

class UniversityDetailView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = University.objects.all()
    serializer_class = UniversitySerializer