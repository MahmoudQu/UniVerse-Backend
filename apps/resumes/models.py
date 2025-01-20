# apps/resumes/models.py
from django.db import models
from apps.students.models import Student


class Resume(models.Model):
    file_name = models.CharField(max_length=50)
    file_url = models.URLField(null=True, blank=True)
    student = models.ForeignKey(
        Student, on_delete=models.CASCADE, related_name='resumes')
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.file_name
