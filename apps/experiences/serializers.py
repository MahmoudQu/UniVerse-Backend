from rest_framework import serializers
from .models import Experience

class EducationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Experience
        fields = ['id', 'position', 'company', 'start_date', 'end_date', 'student']
