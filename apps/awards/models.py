from django.db import models
from apps.students.models import Student


class Award(models.Model):
    student = models.ForeignKey(Student, null=True,
                                blank=True, on_delete=models.SET_NULL, related_name='awards')
    title = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    start_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.title
