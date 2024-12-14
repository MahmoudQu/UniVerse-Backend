from rest_framework import serializers
from .models import Award

class AwardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Award
        fields = ['id', 'student', 'title', 'description', 'start_date', 'created_at', 'updated_at']
