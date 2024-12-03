from rest_framework import serializers
from .models import University, Department


class UniversitySerializer(serializers.ModelSerializer):
    class Meta:
        model = University
        fields = ['id', 'name', 'address', 'website_url', 'contact_email', 'contact_phone']


class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = ['id', 'name', 'university']
