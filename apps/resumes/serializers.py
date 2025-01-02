from rest_framework import serializers
from .models import Resume

class ResumeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Resume
        fields = ['id', 'file_name', 'file_url', 'student']

    def create(self, validated_data):
        return Resume.objects.create(**validated_data)