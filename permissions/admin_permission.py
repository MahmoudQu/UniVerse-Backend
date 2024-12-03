from rest_framework import permissions

class IsAdminUser(permissions.BasePermission):
    """
    Custom permission to grant access only to admin users.
    """

    def has_permission(self, request, view):
        # Check if the user is authenticated and is an admin
        return request.user.is_authenticated and hasattr(request.user, 'admin')