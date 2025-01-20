from django.urls import path
from .views import PendingSignupRequestListView, AcceptSignupRequestView, RejectSignupRequestView

urlpatterns = [
    path('pending_signup_requests/', PendingSignupRequestListView.as_view(),
         name='pending_signup_requests'),
    path('pending_signup_requests/<int:pk>/accept/',
         AcceptSignupRequestView.as_view(), name='accept_request'),
    path('pending_signup_requests/<int:pk>/reject/',
         RejectSignupRequestView.as_view(), name='reject_request'),
]
