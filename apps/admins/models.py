from django.db import models
from django.contrib.auth.hashers import make_password, check_password
from apps.accounts.models import CustomUser

class Admin(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, default=3)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    is_admin = models.BooleanField(default=True)
    status = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return f"Admin: {self.first_name} {self.last_name}"