# apps/educations/models.py
from django.db import models
from apps.students.models import Student


class Education(models.Model):
    field_of_study = models.CharField(max_length=255)
    institute = models.CharField(max_length=255)
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()
    students = models.ManyToManyField(Student, related_name='educations')

    def __str__(self):
        return f"{self.field_of_study} at {self.institute}"
