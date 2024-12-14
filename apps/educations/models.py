# apps/educations/models.py
from django.db import models
from apps.students.models import Student


class Education(models.Model):
    student = models.ForeignKey(Student, null=True,
                                blank=True, on_delete=models.SET_NULL, related_name='educations')
    field_of_study = models.CharField(max_length=255)
    institute = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    start_date = models.DateField()
    end_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return f"{self.field_of_study} at {self.institute}"