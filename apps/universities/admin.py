from django.contrib import admin
from .models import University
from ..departments.models import Department

admin.site.register(University)
admin.site.register(Department)

