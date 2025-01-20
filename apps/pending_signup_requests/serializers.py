from rest_framework import serializers
from apps.companies.models import Company
from apps.pending_signup_requests.models import PendingSignupRequest


class CompanySerializer(serializers.ModelSerializer):
    email = serializers.SerializerMethodField()

    class Meta:
        model = Company
        fields = ['id', 'name', 'email',
                  'proof_document', 'created_at', 'updated_at']

    def get_email(self, obj):
        return obj.user.email


class PendingSignupRequestSerializer(serializers.ModelSerializer):
    company = CompanySerializer()

    class Meta:
        model = PendingSignupRequest
        fields = ['id', 'company']
