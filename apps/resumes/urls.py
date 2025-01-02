from django.urls import path
from .views import ResumeRetrieveUpdateDestroyView, AddCVView, ResumeListView, StudentResumesView

urlpatterns = [
    path('resumes/', ResumeListView.as_view(), name='resume_list_create'),
    path('resumes/<int:pk>/', ResumeRetrieveUpdateDestroyView.as_view(), name='resume_retrieve_update_destroy'),
    path('add_resume/', AddCVView.as_view(), name='add_resume'),
    path('students/<int:student_id>/resumes/', StudentResumesView.as_view(), name='student_resumes'),
]