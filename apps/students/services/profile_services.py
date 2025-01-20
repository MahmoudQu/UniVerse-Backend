from apps.resumes.models import Resume
from apps.students.models import Student
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
import cloudinary.uploader


def handle_student_profile_update(request):
    from apps.students.serializers import StudentSerializer

    student = get_object_or_404(Student, user=request.user)
    serializer = StudentSerializer(student, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response({"detail": "Your profile updated successfully."}, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


def add_user_cv(request):
    user = request.user
    if not user.is_authenticated:
        return Response(
            {"detail": "Authentication credentials were not provided."},
            status=status.HTTP_401_UNAUTHORIZED
        )

    files = request.FILES.getlist('files')  # Retrieve multiple files
    if not files:
        return Response(
            {"detail": "At least one CV file is required."},
            status=status.HTTP_400_BAD_REQUEST
        )

    uploaded_files = []
    skipped_files = []

    try:
        for file in files:
            file_name = file.name

            # Check if the file already exists for the user
            existing_file = Resume.objects.filter(
                student=user.student, file_name=file_name).first()

            if existing_file:
                skipped_files.append(file_name)
                continue


            # Upload the file to Cloudinary
            result = cloudinary.uploader.upload(
                file,
                resource_type="raw",
                content_type="application/pdf",
                format="pdf"  # Ensure the file format
            )
            file_url = result.get('secure_url')  # Use the URL as returned by Cloudinary
            print(f"Uploaded file URL: {file_url}")

            # Save the file record in the database
            Resume.objects.create(
                file_name=file_name,
                file_url=file_url,
                student=user.student,
            )
            uploaded_files.append(file_name)

        return Response(
            {
                "detail": "Files processed successfully.",
                "uploaded_files": uploaded_files,
                "skipped_files": skipped_files,
            },
            status=status.HTTP_200_OK
        )

    except Exception as e:
        return Response(
            {
                "detail": "An error occurred while uploading files.",
                "error": str(e),
            },
            status=status.HTTP_500_INTERNAL_SERVER_ERROR
        )
