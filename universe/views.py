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
    try:
        with connection.cursor() as cursor:
            # Get the list of all tables
            cursor.execute(
                "SELECT table_name FROM information_schema.tables WHERE table_schema = 'public'")
            tables = cursor.fetchall()

            # Construct and execute the TRUNCATE command for all tables
            for table in tables:
                table_name = table[0]
                cursor.execute(f"TRUNCATE TABLE {
                               table_name} RESTART IDENTITY CASCADE;")

        return Response({"detail": "All tables truncated successfully."}, status=status.HTTP_200_OK)

    except OperationalError as e:
        return Response({"detail": f"Error truncating tables: {str(e)}"}, status=status.HTTP_400_BAD_REQUEST)
