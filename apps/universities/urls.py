from django.urls import path
from .views import (
    UniversityListCreateView, UniversityDetailView,
    DepartmentListCreateView, DepartmentDetailView,
    DepartmentsByUniversityView
)

urlpatterns = [
    path('universities/', UniversityListCreateView.as_view(), name='university-list-create'),
    path('universities/<int:pk>/', UniversityDetailView.as_view(), name='university-detail'),
    path('departments/', DepartmentListCreateView.as_view(), name='department-list-create'),
    path('departments/<int:pk>/', DepartmentDetailView.as_view(), name='department-detail'),
    path('universities/<int:university_id>/departments/', DepartmentsByUniversityView.as_view(), name='departments-by-university'),
]
