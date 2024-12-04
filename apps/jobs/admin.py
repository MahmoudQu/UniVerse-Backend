from django.contrib import admin
from .models import JobPost, Application, SavedJob

admin.site.register(JobPost)
admin.site.register(Application)
admin.site.register(SavedJob)


