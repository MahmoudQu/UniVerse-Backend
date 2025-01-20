from django.db import models

class University(models.Model):
    name = models.CharField(max_length=255)
    address = models.TextField(null=True, blank=True)
    website_url = models.URLField(null=True, blank=True)
    contact_email = models.EmailField(null=True, blank=True)
    contact_phone = models.CharField(max_length=15, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.name