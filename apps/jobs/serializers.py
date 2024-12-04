from rest_framework import serializers
from .models import JobPost, Application, SavedJob


class JobPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = JobPost
        fields = ['id', 'title', 'description', 'location', 'company', 'type']


class ApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Application
        fields = ['id', 'status', 'student', 'job_post', 'resume_id']


class SavedJobSerializer(serializers.ModelSerializer):
    class Meta:
        model = SavedJob
        fields = ['id', 'student', 'job_post']
