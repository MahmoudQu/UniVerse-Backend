from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import PendingSignupRequest
from apps.companies.models import Company
from .serializers import PendingSignupRequestSerializer, CompanySerializer
from rest_framework import generics, permissions



class PendingSignupRequestListView(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = PendingSignupRequest.objects.all()
    serializer_class = PendingSignupRequestSerializer


class AcceptSignupRequestView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    def post(self, request, pk):
        pending_request = PendingSignupRequest.objects.get(pk=pk)
        company = pending_request.company
        company.is_accepted = True
        company.save()
        pending_request.delete()
        return Response({"detail": "Company accepted successfully."}, status=status.HTTP_200_OK)


class RejectSignupRequestView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    def post(self, request, pk):
        pending_request = PendingSignupRequest.objects.get(pk=pk)
        pending_request.delete()
        return Response({"detail": "Company rejected successfully."}, status=status.HTTP_200_OK)
