from django.urls import path
from .views import ExperienceListCreateView, ExperienceRetrieveUpdateDestroyView

urlpatterns = [
    path('experiences/', ExperienceListCreateView.as_view(), name='experience-list-create'),
    path('experiences/<int:pk>/', ExperienceRetrieveUpdateDestroyView.as_view(), name='experience-retrieve-update-destroy'),
]