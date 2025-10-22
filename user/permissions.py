from rest_framework import permissions


class AllowAnyForPost(permissions.BasePermission):
    """
    Allow POST without authentication (for user registration),
    but require authentication for other methods
    """

    def has_permission(self, request, view):
        if request.method == "POST":
            return True
        return request.user and request.user.is_authenticated
