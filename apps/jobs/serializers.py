from rest_framework import serializers

from apps.companies.models import Company
from apps.departments.models import Department
from .models import JobPost, Application, SavedJob
from custom.fields.CommaSeparatedListField import CommaSeparatedListField
from apps.companies.serializers import CompanySerializer
from apps.departments.serializers import DepartmentSerializer
from apps.resumes.models import Resume
from rest_framework.exceptions import ValidationError


class JobPostSerializer(serializers.ModelSerializer):
    tags = serializers.ListField(
        child=serializers.CharField(), allow_null=True, required=False)
    requirements = serializers.ListField(
        child=serializers.CharField(), allow_null=True, required=False)

    # Nested serializers for read operations
    company = CompanySerializer(read_only=True)
    department = DepartmentSerializer(read_only=True)

    # ID fields for write operations
    company_id = serializers.PrimaryKeyRelatedField(
        queryset=Company.objects.all(), source='company', write_only=True
    )
    department_id = serializers.PrimaryKeyRelatedField(
        queryset=Department.objects.all(), source='department', write_only=True
    )

    class Meta:
        model = JobPost
        fields = [
            'id', 'title', 'description', 'company', 'company_id',
            'department', 'department_id', 'type', 'salary_range',
            'tags', 'requirements', 'created_at', 'updated_at', 'status'
        ]


class ApplicationSerializer(serializers.ModelSerializer):
    resume_id = serializers.PrimaryKeyRelatedField(
        queryset=Resume.objects.all(), source='resume', write_only=True
    )
    resume = serializers.StringRelatedField(
        read_only=True)  # For display purposes

    class Meta:
        model = Application
        fields = ['id', 'status', 'student', 'job_post', 'resume_id', 'resume']

    def create(self, validated_data):
        student = validated_data['student']
        job_post = validated_data['job_post']

# Check if the student has already applied for the job
        if Application.objects.filter(student=student, job_post=job_post).exists():
            raise ValidationError(
                {"detail": "You have applied for this job before."})

        return super().create(validated_data)


class SavedJobSerializer(serializers.ModelSerializer):
    class Meta:
        model = SavedJob
        fields = ['id', 'student', 'job_post']


class JobPostWithApplicationSerializer(serializers.ModelSerializer):
    application = serializers.SerializerMethodField()
    company = CompanySerializer(read_only=True)
    department = DepartmentSerializer(read_only=True)

    class Meta:
        model = JobPost
        fields = ['id', 'title', 'description', 'company', 'department', 'type', 'salary_range',
                  'tags', 'requirements', 'status', 'created_at', 'updated_at', 'application']

    def get_application(self, obj):
        request = self.context.get('request')
        student = request.user.student
        application = Application.objects.filter(
            student=student, job_post=obj).first()
        return ApplicationSerializer(application).data if application else None
