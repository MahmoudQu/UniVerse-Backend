from rest_framework import serializers

from custom.fields.CommaSeparatedListField import CommaSeparatedListField
from .models import Student
from apps.accounts.models import CustomUser
from apps.departments.models import Department
from apps.universities.models import University
from apps.universities.serializers import UniversitySerializer
from apps.departments.serializers import DepartmentSerializer


class StudentSerializer(serializers.ModelSerializer):

    university = UniversitySerializer(read_only=True)
    department = DepartmentSerializer(read_only=True)

    department_id = serializers.PrimaryKeyRelatedField(
        queryset=Department.objects.all(), source='department', write_only=True, required=False
    )
    university_id = serializers.PrimaryKeyRelatedField(
        queryset=University.objects.all(), source='university', write_only=True, required=False
    )

    email = serializers.EmailField(write_only=True)
    password = serializers.CharField(write_only=True)
    is_verified = serializers.BooleanField(read_only=True)
    user = serializers.PrimaryKeyRelatedField(read_only=True)
    skills = CommaSeparatedListField(allow_null=True, required=False)

    class Meta:
        model = Student
        fields = [
            'id', 'user', 'first_name', 'last_name', 'email', 'password',
            'is_verified', 'image', 'phone', 'department', 'university',
            'date_of_birth', 'github', 'linkedin', 'portfolio', 'skills', 'department_id', 'university_id'
        ]

    def create(self, validated_data):
        email = validated_data.pop('email')
        password = validated_data.pop('password')
        user = CustomUser.objects.create_user(
            email=email,
            password=password
        )
        student = Student.objects.create(
            user=user,
            **validated_data
        )
        return student

    def update(self, instance, validated_data):
        # Remove 'email' if it's in the validated data
        validated_data.pop('email', None)
        return super().update(instance, validated_data)
