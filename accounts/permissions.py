from rest_framework import permissions
from rest_framework.views import Request, View


class IsAdminOnGetRoute(permissions.BasePermission):
    def has_permission(self, request: Request, view: View) -> bool:
        return (
            request.method != "GET" and request.method != "POST"
        ) or request.user.is_superuser


class IsAdminOrCritic(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user.is_superuser or request.user.is_critic:
            return True

    def has_object_permission(self, request, view, obj):
        return request.user == obj or request.user.is_superuser
