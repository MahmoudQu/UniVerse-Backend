from django.shortcuts import render
# Create your views here.
from rest_framework import generics, permissions

from apps.students.serializers import StudentSerializer
from .models import JobPost, Application, SavedJob
from .serializers import JobPostSerializer, ApplicationSerializer, SavedJobSerializer, JobPostWithApplicationSerializer
from permissions import student_permission, company_permission
from apps.students.models import Student
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from django.core.mail import send_mail
from rest_framework import status


class DeleteApplicationView(generics.DestroyAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Application.objects.all()
    serializer_class = ApplicationSerializer

    def destroy(self, request, *args, **kwargs):
        application = self.get_object()
        application.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class ApproveApplicationView(generics.UpdateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Application.objects.all()
    serializer_class = ApplicationSerializer

    def update(self, request, *args, **kwargs):
        application = self.get_object()
        application.status = "Approved"
        application.save()

        # Send email to the student
        send_mail(
            'Application Approved',
            f'Your application to {application.job_post.title} at {
                application.job_post.company.name} has been approved, we will contact you soon.',
            request.user.email,  # Assuming the company email is available in the request user
            # Assuming the student has a user with an email
            [application.student.user.email],
            fail_silently=False,
        )

        return Response(self.get_serializer(application).data, status=status.HTTP_200_OK)


class RejectApplicationView(generics.UpdateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Application.objects.all()
    serializer_class = ApplicationSerializer

    def update(self, request, *args, **kwargs):
        application = self.get_object()
        application.status = "Rejected"
        application.save()

        return Response(self.get_serializer(application).data, status=status.HTTP_200_OK)


class JobApplicantsView(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = ApplicationSerializer

    def get_queryset(self):
        job_post_id = self.kwargs['job_post_id']
        job_post = get_object_or_404(
            JobPost, id=job_post_id, company=self.request.user.company)
        return Application.objects.filter(job_post=job_post)

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        return Response(self.custom_representation(queryset))

    def custom_representation(self, queryset):
        data = []
        for application in queryset:
            student = application.student
            student_data = {
                'image': student.image,
                'first_name': student.first_name,
                'last_name': student.last_name,
                'university': student.university.name,
                'department': student.department.name,
                'phone': student.phone,
                'id': student.id
            }
            data.append({
                'id': application.id,
                'status': application.status,
                'student': student_data,
                'job_post': application.job_post.title,
                'resume': application.resume.file_url
            })
        return data


class StudentAppliedJobsView(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = JobPostWithApplicationSerializer

    def get_queryset(self):
        student = self.request.user.student
        applied_jobs = Application.objects.filter(
            student=student).values_list('job_post', flat=True)
        return JobPost.objects.filter(id__in=applied_jobs)

    def get_serializer_context(self):
        # Pass the request to the serializer context
        context = super().get_serializer_context()
        context['request'] = self.request
        return context


class FeaturedJobsView(generics.ListAPIView):
    serializer_class = JobPostSerializer

    def get_queryset(self):
        # Get the logged-in user
        user = self.request.user

        # Ensure the user is a student
        student = get_object_or_404(Student, user=user)
        department = student.department

        if department:
            # Return jobs matching the student's department
            return JobPost.objects.filter(department=department).order_by('?')[:9]
        else:
            # Return 9 random jobs from different departments
            return JobPost.objects.order_by('?')[:9]


class JobPostListCreateView(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = JobPost.objects.all()
    serializer_class = JobPostSerializer


class CompanyJobPostsView(generics.ListAPIView):
    serializer_class = JobPostSerializer

    def get_queryset(self):
        company_id = self.kwargs['company_id']
        return JobPost.objects.filter(company_id=company_id)


class JobPostDetailView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = JobPost.objects.all()
    serializer_class = JobPostSerializer


class ApplicationListCreateView(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Application.objects.all()
    serializer_class = ApplicationSerializer


class ApplicationDetailView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Application.objects.all()
    serializer_class = ApplicationSerializer


class SavedJobListCreateView(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = SavedJob.objects.all()
    serializer_class = SavedJobSerializer


class SavedJobDetailView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = SavedJob.objects.all()
    serializer_class = SavedJobSerializer
