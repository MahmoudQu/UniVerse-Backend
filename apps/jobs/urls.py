from django.urls import path
from .views import (
    JobPostListCreateView, JobPostDetailView,
    ApplicationListCreateView, ApplicationDetailView,
    SavedJobListCreateView, SavedJobDetailView, CompanyJobPostsView,
    FeaturedJobsView, StudentAppliedJobsView, JobApplicantsView,
    ApproveApplicationView, RejectApplicationView, DeleteApplicationView
)

urlpatterns = [
    path('job_posts/', JobPostListCreateView.as_view(),
         name='jobpost_list_create'),
    path('job_posts/<int:pk>/', JobPostDetailView.as_view(), name='jobpost_detail'),
    path('companies/<int:company_id>/job-posts/', CompanyJobPostsView.as_view()),
    path('job_posts/<int:job_post_id>/applicants/',
         JobApplicantsView.as_view(), name='job_applicants'),

    path('applications/', ApplicationListCreateView.as_view(),
         name='application_list_create'),
    path('applications/<int:pk>/', ApplicationDetailView.as_view(),
         name='application_detail'),

    path('saved_jobs/', SavedJobListCreateView.as_view(),
         name='savedjob-list_create'),
    path('saved_jobs/<int:pk>/', SavedJobDetailView.as_view(),
         name='savedjob_detail'),
    path('featured_jobs/', FeaturedJobsView.as_view(), name='featured_jobs'),
    path('students/<int:student_id>/applied_jobs/',
         StudentAppliedJobsView.as_view(), name='student_applied_jobs'),
    path('applications/<int:pk>/approve/',
         ApproveApplicationView.as_view(), name='approve_application'),
    path('applications/<int:pk>/reject/',
         RejectApplicationView.as_view(), name='reject_application'),
    path('applications/<int:pk>/delete/',
         DeleteApplicationView.as_view(), name='delete_application'),
]
