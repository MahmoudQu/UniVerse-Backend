from django.db import models
from apps.students.models import Student
from apps.companies.models import Company


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
    type = models.CharField(max_length=2, choices=JOB_TYPE_CHOICES)

    def __str__(self):
        return self.title


class Application(models.Model):
    STATUS_CHOICES = [
        ('P', 'Pending'),
        ('A', 'Accepted'),
        ('R', 'Rejected'),
    ]

    status = models.CharField(max_length=1, choices=STATUS_CHOICES, default='P')
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name="applications")
    job_post = models.ForeignKey(JobPost, on_delete=models.CASCADE, related_name="applications")
    resume_id = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.student} - {self.job_post}"


class SavedJob(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name="saved_jobs")
    job_post = models.ForeignKey(JobPost, on_delete=models.CASCADE, related_name="saved_by_students")

    class Meta:
        unique_together = ('student', 'job_post')

    def __str__(self):
        return f"{self.student} saved {self.job_post}"

