# apps/jobs/models.py
from django.db import models
from apps.students.models import Student
from apps.companies.models import Company
from apps.departments.models import Department
from apps.resumes.models import Resume
from custom.fields.CommaSeparatedListField import CommaSeparatedListField
from django.utils import timezone


class JobPost(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    company = models.ForeignKey(
        Company, on_delete=models.CASCADE, related_name="job_posts")
    department = models.ForeignKey(
        Department, on_delete=models.CASCADE, related_name="job_posts", null=True, blank=True)
    type = models.CharField(
        max_length=255, null=True, blank=True)
    salary_range = models.CharField(max_length=255, null=True, blank=True)
    tags = models.JSONField(null=True, blank=True, default=list)
    requirements = models.JSONField(null=True, blank=True, default=list)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)
    end_date = models.DateTimeField(null=True, blank=True)
    _is_active = models.BooleanField(default=True, db_column='is_active')

    def is_expired(self):
        if self.end_date:
            return timezone.now() > self.end_date
        return False

    @property
    def is_active(self):
        # Override the is_active property to consider both manual activation and expiration date
        return not self.is_expired() and self._is_active

    def __str__(self):
        return self.title


class Application(models.Model):
    status = models.CharField(max_length=50, default='Pending')
    student = models.ForeignKey(
        Student, on_delete=models.CASCADE, related_name="applications")
    job_post = models.ForeignKey(
        JobPost, on_delete=models.CASCADE, related_name="applications")
    resume = models.ForeignKey('resumes.Resume', on_delete=models.CASCADE,
                               related_name='applications', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.student} applied for {self.job_post}"


class SavedJob(models.Model):
    student = models.ForeignKey(
        Student, on_delete=models.CASCADE, related_name="saved_jobs")
    job_post = models.ForeignKey(
        JobPost, on_delete=models.CASCADE, related_name="saved_by_students")
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        unique_together = ('student', 'job_post')

    def __str__(self):
        return f"{self.student} saved {self.job_post}"
