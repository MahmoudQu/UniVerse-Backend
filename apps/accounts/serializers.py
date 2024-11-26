# apps/accounts/serializers.py

from rest_framework import serializers
from apps.accounts.models import CustomUser
from apps.students.serializers import StudentSerializer
from apps.companies.serializers import CompanySerializer


class UserSerializer(serializers.ModelSerializer):
    data = serializers.SerializerMethodField()

    class Meta:
        model = CustomUser
        fields = ['id', 'email', 'data']  # Include other user fields as needed

    def get_data(self, obj):
        # Determine the user_type based on related profiles
        if hasattr(obj, 'student'):
            return StudentSerializer(obj.student).data
        elif hasattr(obj, 'company'):
            return CompanySerializer(obj.company).data
        else:
            return None

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        request = self.context.get('request')
        user_type = request.data.get('user_type') if request else None

        if user_type == 'company':
            representation.pop('student', None)
        else:
            representation.pop('company', None)

        return representation
