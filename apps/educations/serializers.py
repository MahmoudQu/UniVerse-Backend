from rest_framework import serializers
from .models import Education

class EducationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Education
        fields = ['id', 'field_of_study', 'institute', 'description', 'start_date', 'end_date', 'student', 'created_at', 'updated_at']
