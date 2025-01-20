from rest_framework import serializers
from .models import Experience
from datetime import date


class ExperienceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Experience
        fields = ['id', 'position', 'company', 'description', 'start_date',
                  'end_date', 'student', 'created_at', 'updated_at', 'present', 'status']

    def validate(self, data):
        end_date = data.get('end_date')
        if end_date and end_date > date.today():
            raise serializers.ValidationError({
                'end_date': 'End date cannot be in the future.'
            })
        return data
