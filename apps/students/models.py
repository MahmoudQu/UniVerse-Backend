# apps/students/models.py
from django.db import models
from django.utils import timezone
import uuid
from apps.accounts.models import CustomUser
from apps.universities.models import University
from apps.departments.models import Department
from apps.skills.models import Skill  # Assuming you have an app for skills


class Student(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=255, default='Unknown')
    last_name = models.CharField(max_length=255, default='Unknown')
    is_verified = models.BooleanField(default=False)
    image = models.TextField(null=True, blank=True, default=None)
    phone = models.BigIntegerField(
        null=True, blank=True, unique=True, default=None)
    department = models.ForeignKey(Department, null=True,
                                   blank=True, on_delete=models.SET_NULL)
    university = models.ForeignKey(
        University, null=True, blank=True, on_delete=models.SET_NULL)
    date_of_birth = models.DateField(null=True, blank=True)
    github = models.URLField(max_length=255, null=True, blank=True)
    linkedin = models.URLField(max_length=255, null=True, blank=True)
    portfolio = models.URLField(max_length=255, null=True, blank=True)
    about = models.TextField(null=True, blank=True)
    skills = models.TextField(null=True, blank=True, default="")

    def generate_otp(self):
        self.user.otp = str(uuid.uuid4().int)[:6]
        self.user.otp_expiration = timezone.now() + timezone.timedelta(minutes=10)
        self.user.save()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
