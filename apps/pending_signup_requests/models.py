from django.db import models
from apps.companies.models import Company


class PendingSignupRequest(models.Model):
    company = models.OneToOneField(
        Company, on_delete=models.CASCADE, related_name='pending_request')

    def __str__(self):
        return f"Pending request for {self.company.name}"
