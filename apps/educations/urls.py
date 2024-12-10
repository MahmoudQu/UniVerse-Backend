from django.urls import path
from .views import EducationListCreateView, EducationDetailView

urlpatterns = [
    path('educations/', EducationListCreateView.as_view(), name='education-list-create'),
    path('educations/<int:pk>/', EducationDetailView.as_view(), name='education-detail'),
]
