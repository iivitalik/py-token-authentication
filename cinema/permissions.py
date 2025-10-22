from rest_framework import permissions


class IsAdminOrIfAuthenticatedReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        if not request.user or not request.user.is_authenticated:
            return False

        if request.method in permissions.SAFE_METHODS:
            return True

        return bool(request.user and request.user.is_staff)


class IsAdminOrOwner(permissions.BasePermission):
    """
    Custom permission for Order:
    - Admin: full access to all orders
    - Authenticated users: full access to their own orders only
    - Anonymous: no access
    """

    def has_permission(self, request, view):
        if not request.user or not request.user.is_authenticated:
            return False

        return True

    def has_object_permission(self, request, view, obj):
        if request.user and request.user.is_staff:
            return True

        return obj.user == request.user
