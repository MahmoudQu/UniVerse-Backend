from rest_framework import serializers
from .models import Experience

class ExperienceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Experience
        fields = ['id', 'position', 'company', 'description', 'start_date', 'end_date', 'student', 'created_at', 'updated_at']