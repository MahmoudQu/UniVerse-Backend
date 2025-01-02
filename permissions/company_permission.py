# permissions/company_permission.py
from rest_framework import permissions


class IsCompany(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and hasattr(request.user, 'company')
