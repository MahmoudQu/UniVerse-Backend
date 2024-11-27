from rest_framework.response import Response
from rest_framework import status
from apps.accounts.serializers import UserSerializer
from .token_services import generate_refresh_token


def get_user_data(request):
    user = request.user
    if user.is_authenticated:
        token = request.auth.key if hasattr(request.auth, 'key') else None

        # Set is_logged_in to True
        user.is_logged_in = True
        user.save(update_fields=['is_logged_in'])

        # Determine the user_type based on related profiles
        if hasattr(user, 'student'):
            user_type = 'student'
        elif hasattr(user, 'company'):
            user_type = 'company'
        else:
            user_type = 'unknown'

        # Generate a refresh token
        refresh_token = generate_refresh_token(user)

        # Serialize the user data
        serializer = UserSerializer(user, context={'request': request})

        return Response(
            {
                "token": token,
                "refresh_token": refresh_token,
                "user_type": user_type,
                "is_logged_in": user.is_logged_in,
                "user": serializer.data
            },
            status=status.HTTP_200_OK
        )
    else:
        return Response(
            {"detail": "Authentication credentials were not provided."},
            status=status.HTTP_401_UNAUTHORIZED
        )
