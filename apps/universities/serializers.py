from rest_framework import serializers
from .models import University

class UniversitySerializer(serializers.ModelSerializer):
    class Meta:
        model = University
        fields = ['id', 'name', 'address', 'website_url', 'contact_email', 'contact_phone', 'created_at', 'updated_at', 'status']