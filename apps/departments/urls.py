from django.urls import path
from .views import DepartmentListCreateView, DepartmentDetailView, DepartmentJobsView

urlpatterns = [
    path('departments/', DepartmentListCreateView.as_view(), name='department-list'),
    path('departments/<int:pk>/', DepartmentDetailView.as_view(),
         name='department-detail'),
    path('departments/<int:department_id>/jobs/',
         DepartmentJobsView.as_view(),
         name='department-jobs'),
]
