from django.urls import path
from .views import (
    JobPostListCreateView, JobPostDetailView,
    ApplicationListCreateView, ApplicationDetailView,
    SavedJobListCreateView, SavedJobDetailView
)

urlpatterns = [
    path('job_posts/', JobPostListCreateView.as_view(), name='jobpost_list_create'),
    path('job_posts/<int:pk>/', JobPostDetailView.as_view(), name='jobpost_detail'),

    path('applications/', ApplicationListCreateView.as_view(), name='application_list_create'),
    path('applications/<int:pk>/', ApplicationDetailView.as_view(), name='application_detail'),

    path('saved_jobs/', SavedJobListCreateView.as_view(), name='savedjob-list_create'),
    path('saved_jobs/<int:pk>/', SavedJobDetailView.as_view(), name='savedjob_detail'),
]
