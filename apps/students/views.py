from rest_framework import generics, permissions
from rest_framework.views import APIView
from .serializers import StudentSerializer
from .models import Student
from apps.authentication.services.main import (
    handle_student_signup,
    handle_student_otp_verification,
    handle_student_new_otp,
)
from .services.profile_services import handle_student_profile_update
from apps.companies.models import Company
from rest_framework.exceptions import PermissionDenied
from rest_framework.response import Response
from rest_framework import status
from apps.educations.models import Education
from apps.experiences.models import Experience
from apps.awards.models import Award
from apps.educations.serializers import EducationSerializer
from apps.experiences.serializers import ExperienceSerializer
from apps.awards.serializers import AwardSerializer
from django.db.models import Q


class StudentSearchView(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = StudentSerializer

    def get_queryset(self):
        queryset = Student.objects.all()
        search_term = self.request.query_params.get('search', None)
        department_id = self.request.query_params.get('department', None)

        if search_term:
            queryset = queryset.filter(
                Q(first_name__icontains=search_term) |
                Q(last_name__icontains=search_term) |
                Q(skills__contains=[search_term])
            )

        if department_id:
            queryset = queryset.filter(department_id=department_id)

        return queryset


class FeaturedStudentsView(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = StudentSerializer

    def get_queryset(self):
        # Get the logged-in user
        user = self.request.user

        # Check if the user is associated with a company
        try:
            company = user.company  # Assuming OneToOneField from CustomUser to Company
        except Company.DoesNotExist:
            raise PermissionDenied(
                "You must be logged in as a company to access this endpoint.")

        # Get the department of the company
        department = company.department if hasattr(
            company, 'department') else None

        if department:
            # Return 9 students from the same department
            return Student.objects.filter(department=department).order_by('?')[:9]
        else:
            # Return 9 random students
            return Student.objects.order_by('?')[:9]


class StudentListCreateView(generics.ListCreateAPIView):
    permission_classes = [permissions.AllowAny]
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


class StudentDetailView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.AllowAny]
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


class StudentSignupView(generics.CreateAPIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = StudentSerializer

    def create(self, request, *args, **kwargs):
        return handle_student_signup(request)


class StudentVerifyOTPView(generics.CreateAPIView):
    permission_classes = [permissions.AllowAny]

    def create(self, request, *args, **kwargs):
        return handle_student_otp_verification(request)


class StudentRequestNewOTPView(generics.CreateAPIView):
    permission_classes = [permissions.AllowAny]

    def create(self, request, *args, **kwargs):
        return handle_student_new_otp(request)


class StudentUpdateProfileView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def put(self, request, *args, **kwargs):
        return handle_student_profile_update(request)


class StudentResumeInfoView(generics.RetrieveAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Student.objects.all()
    lookup_field = 'id'  # Use 'id' as the lookup field

    def get(self, request, *args, **kwargs):
        student = self.get_object()

        educations = Education.objects.filter(student=student)
        experiences = Experience.objects.filter(student=student)
        awards = Award.objects.filter(student=student)

        education_serializer = EducationSerializer(educations, many=True)
        experience_serializer = ExperienceSerializer(experiences, many=True)
        award_serializer = AwardSerializer(awards, many=True)

        data = {
            "educations": education_serializer.data,
            "experiences": experience_serializer.data,
            "awards": award_serializer.data
        }

        return Response(data, status=status.HTTP_200_OK)
