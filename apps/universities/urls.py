from django.urls import path
from .views import (
    UniversityListCreateView, UniversityDetailView,
    MajorListCreateView, MajorDetailView,
    MajorsByUniversityView
)

urlpatterns = [
    path('universities/', UniversityListCreateView.as_view(), name='university-list-create'),
    path('universities/<int:pk>/', UniversityDetailView.as_view(), name='university-detail'),

    path('majors/', MajorListCreateView.as_view(), name='major-list-create'),
    path('majors/<int:pk>/', MajorDetailView.as_view(), name='major-detail'),

    path('universities/<int:university_id>/majors/', MajorsByUniversityView.as_view(), name='majors-by-university'),
]
