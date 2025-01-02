from django.shortcuts import render
from rest_framework import generics, permissions
from .models import Award
from .serializers import AwardSerializer
from permissions import student_permission

class AwardListCreateView(generics.ListCreateAPIView):
    permission_classes = [permissions.AllowAny]
    queryset = Award.objects.all()
    serializer_class = AwardSerializer


class AwardDetailView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.AllowAny]
    queryset = Award.objects.all()
    serializer_class = AwardSerializer

