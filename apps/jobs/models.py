# apps/jobs/models.py
from django.db import models
from apps.students.models import Student
from apps.companies.models import Company
from apps.departments.models import Department
from apps.resumes.models import Resume
from custom.fields.CommaSeparatedListField import CommaSeparatedListField


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
    status = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

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

    def __str__(self):
        return f"{self.student} applied for {self.job_post}"


class SavedJob(models.Model):
    student = models.ForeignKey(
        Student, on_delete=models.CASCADE, related_name="saved_jobs")
    job_post = models.ForeignKey(
        JobPost, on_delete=models.CASCADE, related_name="saved_by_students")
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    class Meta:
        unique_together = ('student', 'job_post')

    def __str__(self):
        return f"{self.student} saved {self.job_post}"
