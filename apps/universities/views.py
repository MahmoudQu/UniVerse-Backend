from rest_framework import generics
from .models import University, Department
from .serializers import UniversitySerializer, DepartmentSerializer
from rest_framework import generics, permissions
from permissions.admin_permission import IsAdminUser


class UniversityListCreateView(generics.ListCreateAPIView):
    permission_classes = [IsAdminUser, permissions.IsAuthenticated]
    queryset = University.objects.all()
    serializer_class = UniversitySerializer


class UniversityDetailView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAdminUser, permissions.IsAuthenticated]
    queryset = University.objects.all()
    serializer_class = UniversitySerializer


class DepartmentListCreateView(generics.ListCreateAPIView):
    permission_classes = [IsAdminUser, permissions.IsAuthenticated]
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer


class DepartmentDetailView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAdminUser, permissions.IsAuthenticated]
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer

class DepartmentsByUniversityView(generics.ListAPIView):
    permission_classes = [IsAdminUser, permissions.IsAuthenticated]
    serializer_class = DepartmentSerializer
    
    def get_queryset(self):
        university_id = self.kwargs['university_id']
        return Department.objects.filter(university_id=university_id)
