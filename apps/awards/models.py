from django.db import models
from apps.students.models import Student

class Award(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='awards')
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return self.title
