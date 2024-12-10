# apps/students/serializers.py

from rest_framework import serializers

from custom.fields.CommaSeparatedListField import CommaSeparatedListField
from .models import Student
from apps.accounts.models import CustomUser
# Assuming Department model is in apps.departments
from apps.departments.models import Department
# Assuming University model is in apps.universities
from apps.universities.models import University
from apps.skills.models import Skill  # Assuming Skill model is in apps.skills


class StudentSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(write_only=True)
    password = serializers.CharField(write_only=True)
    is_verified = serializers.BooleanField(read_only=True)
    user = serializers.PrimaryKeyRelatedField(read_only=True)
    department = serializers.PrimaryKeyRelatedField(
        queryset=Department.objects.all(), allow_null=True, required=False
    )
    university = serializers.PrimaryKeyRelatedField(
        queryset=University.objects.all(), allow_null=True, required=False
    )
    skills = CommaSeparatedListField(allow_null=True, required=False)

    class Meta:
        model = Student
        fields = [
            'id', 'user', 'first_name', 'last_name', 'email', 'password',
            'is_verified', 'image', 'phone', 'department', 'university',
            'date_of_birth', 'github', 'linkedin', 'portfolio', 'skills'
        ]

    def create(self, validated_data):
        email = validated_data.pop('email')
        password = validated_data.pop('password')
        # skills_data = validated_data.pop('skills', [])

        user = CustomUser.objects.create_user(
            email=email,
            password=password
        )
        student = Student.objects.create(
            user=user,
            **validated_data
        )
        # if skills_data:
        #     student.skills.set(skills_data)
        return student

    def update(self, instance, validated_data):
        # Remove 'email' if it's in the validated data
        validated_data.pop('email', None)
        return super().update(instance, validated_data)