from rest_framework.response import Response
from rest_framework import status
from apps.accounts.serializers import UserSerializer


def get_user_data(request):
    user = request.user
    if user.is_authenticated:
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

        # Serialize the user data
        serializer = UserSerializer(user, context={'request': request})

        return Response(
            {
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
