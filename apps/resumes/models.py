# apps/resumes/models.py
from django.db import models
from apps.students.models import Student

class Resume(models.Model):
    file_name = models.CharField(max_length=255)
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='resumes')

    def __str__(self):
        return self.file_name