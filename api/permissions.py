from rest_framework import permissions

class IsAdminUserOrReadOnly(permissions.BasePermission):
    """
    Custom permission to only allow admins to edit objects.
    """

    def has_permission(self, request, view):
        # Allow read permissions for all requests.
        if request.method in permissions.SAFE_METHODS:
            return True

        # Restrict write permissions to admin users only.
        return request.user and request.user.is_staff
