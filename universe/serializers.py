# from rest_framework import serializers
# from apps.accounts.models import CustomUser
# from apps.students.models import Student
# from apps.companies.models import Company


# class StudentSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Student
#         fields = ['first_name', 'last_name', 'is_verified']


# class CompanySerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Company
#         fields = ['name', 'is_verified']


# class UserSerializer(serializers.ModelSerializer):
#     student = StudentSerializer(read_only=True)
#     company = CompanySerializer(read_only=True)

#     class Meta:
#         model = CustomUser
#         fields = ['id', 'email', 'student', 'company']
#         extra_kwargs = {'password': {'write_only': True}}

#     def to_representation(self, instance):
#         representation = super().to_representation(instance)
#         request = self.context.get('request')
#         user_type = request.data.get('user_type') if request else None

#         if user_type == 'company':
#             representation.pop('student', None)
#         else:
#             representation.pop('company', None)

#         return representation
