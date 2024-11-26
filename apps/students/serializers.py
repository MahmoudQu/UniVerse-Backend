# apps/students/serializers.py

from rest_framework import serializers
from .models import Student
from apps.accounts.models import CustomUser

class StudentSerializer(serializers.ModelSerializer):
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    email = serializers.EmailField(write_only=True)
    password = serializers.CharField(write_only=True)
    is_verified = serializers.BooleanField(read_only=True)

    class Meta:
        model = Student
        fields = ['first_name', 'last_name', 'email', 'password', 'is_verified']

    def create(self, validated_data):
        first_name = validated_data.pop('first_name')
        last_name = validated_data.pop('last_name')
        email = validated_data.pop('email')
        password = validated_data.pop('password')

        user = CustomUser.objects.create_user(
            email=email,
            password=password
        )
        student = Student.objects.create(
            user=user,
            first_name=first_name,
            last_name=last_name,
            **validated_data
        )
        return student