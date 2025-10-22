from rest_framework import permissions


class IsAdminOrIfAuthenticatedReadOnly(permissions.BasePermission):
    """
    Custom permission to allow:
    - Read-only for authenticated users
    - Full access for admin users
    """

    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS and request.user.is_authenticated:
            return True

        return bool(request.user and request.user.is_staff)
