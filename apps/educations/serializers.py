from rest_framework import serializers
from .models import Education
from datetime import date


class EducationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Education
        fields = ['id', 'field_of_study', 'institute', 'description',
                  'start_date', 'end_date', 'student', 'created_at', 'updated_at', 'present', 'status']

    def validate(self, data):
        end_date = data.get('end_date')
        if end_date and end_date > date.today():
            raise serializers.ValidationError({
                'detail': 'End date cannot be in the future.'
            })
        return data
