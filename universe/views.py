from django.db import connection
from django.http import HttpResponse
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework import status

@api_view(['GET'])
@authentication_classes([SessionAuthentication, TokenAuthentication])
@permission_classes([IsAuthenticated])
def test_token(request):
    return Response("Passed for {}".format(request.user.email))


def home(request):
    return HttpResponse("Welcome to the Universe API!")


@api_view(['POST'])
@permission_classes([AllowAny])
def truncate_tables(request):
    with connection.cursor() as cursor:
        cursor.execute(
            "TRUNCATE TABLE accounts_customuser, students_student, companies_company RESTART IDENTITY CASCADE;")
    return Response({"detail": "All tables truncated successfully."}, status=status.HTTP_200_OK)
