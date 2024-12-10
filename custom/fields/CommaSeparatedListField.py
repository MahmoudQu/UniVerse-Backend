from rest_framework import serializers


class CommaSeparatedListField(serializers.Field):
    def to_internal_value(self, data):
        if not data:
            return ''
        if isinstance(data, list):
            # Convert list to a comma-separated string
            return ', '.join(map(str, data))
        elif isinstance(data, str):
            return data.strip()
        else:
            raise serializers.ValidationError('Expected a list of strings.')

    def to_representation(self, value):
        if not value:
            return []
        # Convert comma-separated string to a list
        return [item.strip() for item in value.split(',')]
