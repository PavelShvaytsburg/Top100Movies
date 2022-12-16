from rest_framework import permissions

class ReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True

        return bool(request.user and request.user.is_staff)

class UpdateRead(permissions.BasePermission):
    def has_permission(self, request, view):
        allowed_methods = ('GET', 'PUT', )
        if request.method in allowed_methods:
            return True

        return bool(request.user and request.user.is_staff)
