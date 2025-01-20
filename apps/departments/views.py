from rest_framework import generics, permissions

from apps.jobs.models import JobPost
from apps.jobs.serializers import JobPostSerializer
from .models import Department
from .serializers import DepartmentSerializer


class DepartmentListCreateView(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer


class DepartmentDetailView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer


class DepartmentJobsView(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = JobPostSerializer

    def get_queryset(self):
        department_id = self.kwargs['department_id']
        return JobPost.objects.filter(department_id=department_id, _is_active=True)
