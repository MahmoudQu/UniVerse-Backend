from apps.accounts.models import CustomUser
from apps.students.models import Student
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404


def handle_student_profile_update(request):
    from apps.students.serializers import StudentSerializer

    student = get_object_or_404(Student, user=request.user)
    serializer = StudentSerializer(student, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response({"message": "Your profile updated successfully."}, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
