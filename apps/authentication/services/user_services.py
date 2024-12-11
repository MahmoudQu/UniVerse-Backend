from rest_framework.response import Response
from rest_framework import status
from apps.accounts.serializers import UserSerializer
from apps.students.serializers import StudentSerializer
from apps.companies.serializers import CompanySerializer
import cloudinary.uploader


def get_user_data(request):
    user = request.user
    if user.is_authenticated:
        # Set is_logged_in to True
        user.is_logged_in = True
        user.save(update_fields=['is_logged_in'])

        # Serialize the user data
        serializer = UserSerializer(user)

        return Response(
            serializer.data,
            status=status.HTTP_200_OK
        )
    else:
        return Response(
            {"detail": "Authentication credentials were not provided."},
            status=status.HTTP_401_UNAUTHORIZED
        )


def get_profile(request):
    user = request.user
    print("User email is", user.email)

    if not user.is_authenticated:
        return Response(
            {"detail": "Authentication credentials were not provided."},
            status=status.HTTP_401_UNAUTHORIZED
        )

    if hasattr(user, 'student'):
        student = user.student
        serializer = StudentSerializer(student)
        response_data = serializer.data  # Serialized data from StudentSerializer
        response_data["email"] = user.email  # Add email to the response
        return Response(response_data, status=status.HTTP_200_OK)

    elif hasattr(user, 'company'):
        company = user.company
        serializer = CompanySerializer(company)
        response_data = serializer.data  # Serialized data from CompanySerializer
        response_data["email"] = user.email  # Add email to the response
        return Response(response_data, status=status.HTTP_200_OK)

    else:
        return Response(
            {"detail": "User profile not found."},
            status=status.HTTP_404_NOT_FOUND
        )


def update_user_image(request):
    user = request.user
    if not user.is_authenticated:
        return Response(
            {"detail": "Authentication credentials were not provided."},
            status=status.HTTP_401_UNAUTHORIZED
        )

    image = request.FILES.get('image')
    if not image:
        return Response(
            {"detail": "Image file is required."},
            status=status.HTTP_400_BAD_REQUEST
        )

    try:
        # Check if the user already has an image and delete it from Cloudinary
        existing_image_url = None
        if hasattr(user, 'student') and user.student.image:
            existing_image_url = user.student.image
        elif hasattr(user, 'company') and user.company.image:
            existing_image_url = user.company.image

        if existing_image_url:
            # Extract the public ID of the existing image from the URL
            public_id = existing_image_url.split("/")[-1].split(".")[0]
            cloudinary.uploader.destroy(public_id)

        # Upload the new image to Cloudinary
        result = cloudinary.uploader.upload(image)
        image_url = result.get('secure_url')

        # Save the new image URL to the user's profile
        if hasattr(user, 'student'):
            user.student.image = image_url
            user.student.save()
        elif hasattr(user, 'company'):
            user.company.image = image_url
            user.company.save()

        return Response({"message": "User image updated successfully."}, status=status.HTTP_200_OK)

    except Exception as e:
        return Response(
            {"detail": "An error occurred while uploading the image.",
             "error": str(e)},
            status=status.HTTP_500_INTERNAL_SERVER_ERROR
        )
