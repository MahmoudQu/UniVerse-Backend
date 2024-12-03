from django.db import models
from apps.accounts.models import CustomUser

class Admin(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)

    def __str__(self):
        return f"Admin: {self.first_name} {self.last_name}"