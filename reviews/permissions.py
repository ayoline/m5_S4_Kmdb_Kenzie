from rest_framework import permissions
from rest_framework.views import Request, View


class IsAdminOrCritic(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method != "GET":
            if request.user.is_authenticated:
                return request.user.is_superuser or request.user.is_critic
            else:
                return False

        return True

    def has_object_permission(self, request, view, obj):
        return request.user.id == obj.critic_id or request.user.is_superuser
