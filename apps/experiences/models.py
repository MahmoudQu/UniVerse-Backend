# apps/experiences/models.py
from django.db import models
from apps.students.models import Student

class Experience(models.Model):
    student = models.ForeignKey(Student, null=True,
                                blank=True, on_delete=models.SET_NULL, related_name='experiences')
    position = models.CharField(max_length=255)
    company = models.CharField(max_length=255)
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return f"{self.position} at {self.company}"