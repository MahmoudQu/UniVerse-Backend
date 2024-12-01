from django.db import models
from django.utils import timezone
import uuid
from apps.accounts.models import CustomUser


class Student(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=30, default='Unknown')
    last_name = models.CharField(max_length=30, default='Unknown')
    is_verified = models.BooleanField(default=False)

    def generate_otp(self):
        self.user.otp = str(uuid.uuid4().int)[:6]
        self.user.otp_expiration = timezone.now() + timezone.timedelta(minutes=10)
        self.user.save()
