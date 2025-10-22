from rest_framework import permissions


class IsAdminOrIfAuthenticatedReadOnly(permissions.BasePermission):
    """
    Custom permission to allow:
    - Read-only for authenticated users
    - Full access for admin users
    - Allow POST (create) for unauthenticated users (user registration)
    """

    def has_permission(self, request, view):
        # Allow POST for unauthenticated users (user registration)
        if request.method == "POST":
            return True

        # Allow read-only for authenticated users
        if (request.method in permissions.SAFE_METHODS
                and request.user.is_authenticated):
            return True

        # Allow full access for admin users
        return bool(request.user and request.user.is_staff)
