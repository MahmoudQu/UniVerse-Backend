from django.urls import path
from .views import (
    JobPostListCreateView, JobPostDetailView,
    ApplicationListCreateView, ApplicationDetailView,
    SavedJobListCreateView, SavedJobDetailView
)

urlpatterns = [
    path('job-posts/', JobPostListCreateView.as_view(), name='jobpost-list-create'),
    path('job-posts/<int:pk>/', JobPostDetailView.as_view(), name='jobpost-detail'),

    path('applications/', ApplicationListCreateView.as_view(), name='application-list-create'),
    path('applications/<int:pk>/', ApplicationDetailView.as_view(), name='application-detail'),

    path('saved-jobs/', SavedJobListCreateView.as_view(), name='savedjob-list-create'),
    path('saved-jobs/<int:pk>/', SavedJobDetailView.as_view(), name='savedjob-detail'),
]
