# apps/companies/serializers.py

from rest_framework import serializers
from .models import Company
from apps.accounts.models import CustomUser


class CompanySerializer(serializers.ModelSerializer):
    email = serializers.EmailField(source='user.email')
    password = serializers.CharField(write_only=True)
    user = serializers.PrimaryKeyRelatedField(read_only=True)
    # proof_document = serializers.FileField(required=True, write_only=True)

    class Meta:
        model = Company
        fields = [
            'id', 'user', 'name', 'email', 'password', 'is_verified',
            'image', 'address', 'phone', 'website_url', 'city', 'country', 'industry', 'about', 'created_at', 'updated_at',
            'status', 'is_accepted', 'proof_document'
        ]

    def create(self, validated_data):
        user_data = validated_data.pop('user', {})
        email = user_data.get('email')
        password = validated_data.pop('password')

        user = CustomUser.objects.create_user(
            email=email,
            password=password
        )
        company = Company.objects.create(
            user=user,
            **validated_data
        )
        return company

    def update(self, instance, validated_data):
        validated_data.pop('user', None)
        validated_data.pop('password', None)
        return super().update(instance, validated_data)
