from django.db import models


class Department(models.Model):
    name = models.CharField(max_length=255, unique=True)
    icon = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.name
