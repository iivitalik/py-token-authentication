from rest_framework import permissions


class IsAdminOrIfAuthenticatedReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):

        # Allow read-only for authenticated users
        if (request.method in permissions.SAFE_METHODS
                and request.user.is_authenticated):
            return True

        # Allow full access for admin users
        return bool(request.user and request.user.is_staff)
