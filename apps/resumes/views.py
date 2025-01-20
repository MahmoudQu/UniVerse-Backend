from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from apps.students.services.profile_services import add_user_cv
from .models import Resume
from .serializers import ResumeSerializer
import cloudinary.uploader
from rest_framework.exceptions import ValidationError
import cloudinary.uploader
from rest_framework import permissions
from rest_framework.views import APIView
from permissions import student_permission


class AddCVView(APIView):
    permission_classes = [permissions.IsAuthenticated,
                          student_permission.IsStudent]

    def post(self, request, *args, **kwargs):
        return add_user_cv(request)


class ResumeListView(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = ResumeSerializer
    queryset = Resume.objects.all()


class ResumeRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Resume.objects.all()
    serializer_class = ResumeSerializer

    def has_object_permission(self, request, view, obj):
        # Check if the user is the owner of the resume
        return obj.student == request.user

    def perform_update(self, serializer):
        file = self.request.FILES.get('file')
        if file:
            result = cloudinary.uploader.upload(file)
            serializer.save(file_name=result.get('secure_url'))
        else:
            serializer.save()

    def perform_destroy(self, instance):
        instance.status = False
        instance.save()


class StudentResumesView(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = ResumeSerializer


    def get_queryset(self):
        student_id = self.kwargs['student_id']
        return Resume.objects.filter(student_id=student_id, status=True)
