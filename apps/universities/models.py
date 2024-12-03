# apps/universities/models.py
from django.db import models

class University(models.Model):
    name = models.CharField(max_length=255)
    address = models.TextField(null=True, blank=True)
    website_url = models.URLField(null=True, blank=True)
    contact_email = models.EmailField(null=True, blank=True)
    contact_phone = models.CharField(max_length=15, null=True, blank=True)

    def __str__(self):
        return self.name

class Department(models.Model):
    name = models.CharField(max_length=255)
    university = models.ForeignKey(University, on_delete=models.CASCADE, related_name="departments")

    def __str__(self):
        return self.name