# apps/jobs/models.py
from django.db import models
from apps.students.models import Student
from apps.companies.models import Company
from apps.resumes.models import Resume  # Assuming you have an app for resumes

class JobPost(models.Model):
    JOB_TYPE_CHOICES = [
        ('FT', 'Full-time'),
        ('PT', 'Part-time'),
        ('IN', 'Internship'),
    ]

    title = models.CharField(max_length=255)
    description = models.TextField()
    location = models.CharField(max_length=255)
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name="job_posts")
    type = models.CharField(max_length=2, choices=JOB_TYPE_CHOICES, null=True, blank=True)
    salary_range = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.title

class Application(models.Model):
    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('Accepted', 'Accepted'),
        ('Rejected', 'Rejected'),
    ]

    status = models.CharField(max_length=255, choices=STATUS_CHOICES, default='Pending')
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name="applications")
    job_post = models.ForeignKey(JobPost, on_delete=models.CASCADE, related_name="applications")
    resume = models.ForeignKey('resumes.Resume', on_delete=models.CASCADE, related_name='applications', null=True, blank=True)

    def __str__(self):
        return f"{self.student} applied for {self.job_post}"

class SavedJob(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name="saved_jobs")
    job_post = models.ForeignKey(JobPost, on_delete=models.CASCADE, related_name="saved_by_students")

    class Meta:
        unique_together = ('student', 'job_post')

    def __str__(self):
        return f"{self.student} saved {self.job_post}"