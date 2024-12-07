# universe/urls.py

from django.contrib import admin
from django.urls import path, include
from .views import truncate_tables

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('apps.authentication.urls')),
    path('api/', include('apps.students.urls')),
    path('api/', include('apps.companies.urls')),
    path('truncate-tables/', truncate_tables, name='truncate_tables'),
    path('api/', include('apps.universities.urls')),
    path('api/', include('apps.departments.urls')),
    path('api/', include('apps.jobs.urls')),

    path('api/', include('apps.awards.urls')),
]
