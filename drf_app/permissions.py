from rest_framework import permissions


class IsAuthorOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        is_safe = request.method in permissions.SAFE_METHODS
        is_author = obj.author == request.user
        return is_author or is_safe
