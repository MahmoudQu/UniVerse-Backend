# apps/accounts/serializers.py

from rest_framework import serializers
from apps.accounts.models import CustomUser
from apps.students.serializers import StudentSerializer
from apps.companies.serializers import CompanySerializer


class UserSerializer(serializers.ModelSerializer):
    user_type = serializers.SerializerMethodField()

    class Meta:
        model = CustomUser
        fields = ['id', 'is_logged_in', 'user_type', 'email']

    def get_user_type(self, obj):
        if hasattr(obj, 'student'):
            return 'student'
        elif hasattr(obj, 'company'):
            return 'company'
        else:
            return 'unknown'
