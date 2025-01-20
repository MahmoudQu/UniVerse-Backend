from apps.accounts.models import CustomUser
from apps.companies.models import Company
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from utils.sendEmailToUser import send_email_to_user
from .otp_services import verify_otp, request_new_otp
import cloudinary.uploader


from apps.accounts.models import CustomUser
from apps.companies.models import Company
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from utils.sendEmailToUser import send_email_to_user
from .otp_services import verify_otp, request_new_otp
import cloudinary.uploader
from apps.companies.serializers import CompanySerializer
from apps.pending_signup_requests.models import PendingSignupRequest


def handle_company_signup(request):
    # Use request.FILES to retrieve the uploaded file
    proof_document = request.FILES.get('proof_document')
    if not proof_document:
        return Response(
            {"detail": "Proof document is required."},
            status=status.HTTP_400_BAD_REQUEST
        )

    try:
        # Upload document to Cloudinary
        result = cloudinary.uploader.upload(
            proof_document,
            resource_type="raw",
            content_type="application/pdf",
            format="pdf"  # Ensure the file format
        )

        # Add the secure URL to the data
        data = request.data.copy()
        data['proof_document'] = result.get('secure_url')

        serializer = CompanySerializer(data=data)
        if serializer.is_valid():
            email = serializer.validated_data['user']['email']
            if CustomUser.objects.filter(email=email).exists():
                return Response(
                    {"detail": "Email already exists."},
                    status=status.HTTP_400_BAD_REQUEST
                )

            # Create company with is_accepted=False by default
            profile = serializer.save()
            user = profile.user
            user.generate_otp()
            user.save()

            # Create a pending signup request
            PendingSignupRequest.objects.create(company=profile)

            send_email_to_user(
                user.email,
                "OTP Verification",
                f"Please verify your email with this OTP: {user.otp}"
            )

            return Response({
                "detail": "Company registration pending approval. Please verify your email with the OTP sent."
            }, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    except Exception as e:
        return Response({
            "detail": "An error occurred while uploading the document.",
            "error": str(e)
        }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


def handle_company_otp_verification(request):
    email = request.data.get('email')
    otp = request.data.get('otp')
    user = get_object_or_404(CustomUser, email=email)
    profile = get_object_or_404(Company, user=user)
    if verify_otp(user, otp):
        profile.is_verified = True
        profile.save()
        return Response({"detail": "Email verified successfully."}, status=status.HTTP_200_OK)
    return Response({"detail": "Invalid or expired OTP."}, status=status.HTTP_400_BAD_REQUEST)


def handle_company_new_otp(request):
    email = request.data.get('email')
    user = get_object_or_404(CustomUser, email=email)
    profile = get_object_or_404(Company, user=user)
    return request_new_otp(user)
