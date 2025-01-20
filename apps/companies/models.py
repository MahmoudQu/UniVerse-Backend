# apps/companies/models.py
from django.db import models
from django.utils import timezone
import uuid
from apps.accounts.models import CustomUser


class Company(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    name = models.CharField(max_length=255, default='Unknown')
    about = models.TextField(null=True, blank=True)
    is_verified = models.BooleanField(default=False)
    image = models.TextField(null=True, blank=True)
    industry = models.CharField(max_length=100, null=True, blank=True)
    address = models.TextField(null=True, blank=True)
    phone = models.CharField(max_length=255, null=True,
                             blank=True, unique=True)
    website_url = models.URLField(max_length=255, null=True, blank=True)
    city = models.CharField(max_length=40, null=True, blank=True)
    country = models.CharField(max_length=40, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)
    status = models.BooleanField(default=True)
    proof_document = models.URLField(null=True, blank=True)
    is_accepted = models.BooleanField(default=False)

    def generate_otp(self):
        self.user.otp = str(uuid.uuid4().int)[:6]
        self.user.otp_expiration = timezone.now() + timezone.timedelta(minutes=10)
        self.user.save()

    def __str__(self):
        return self.name
