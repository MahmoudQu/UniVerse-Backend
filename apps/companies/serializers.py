# apps/companies/serializers.py

from rest_framework import serializers
from .models import Company
from apps.accounts.models import CustomUser


class CompanySerializer(serializers.ModelSerializer):
    name = serializers.CharField()
    email = serializers.EmailField(write_only=True)
    password = serializers.CharField(write_only=True)
    is_verified = serializers.BooleanField(read_only=True)

    class Meta:
        model = Company
        fields = ['name', 'email', 'password', 'is_verified']

    def create(self, validated_data):
        name = validated_data.pop('name')
        email = validated_data.pop('email')
        password = validated_data.pop('password')

        user = CustomUser.objects.create_user(
            email=email,
            password=password
        )
        company = Company.objects.create(
            user=user,
            name=name,
            **validated_data
        )
        return company
