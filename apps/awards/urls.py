from django.urls import path
from .views import AwardListCreateView, AwardDetailView

urlpatterns = [
    path('awards/', AwardListCreateView.as_view(), name='award-list-create'),
    path('awards/<int:pk>/', AwardDetailView.as_view(), name='award-detail'),
]
