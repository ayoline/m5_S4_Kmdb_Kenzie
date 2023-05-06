from rest_framework import permissions
from rest_framework.views import Request, View


class IsAdminAndPostRoute(permissions.BasePermission):
    def has_permission(self, request: Request, view: View) -> bool:
        if request.method == "POST":
            return request.user.is_superuser
        else:
            return True


class IsAdminAndDeleteRoute(permissions.BasePermission):
    def has_permission(self, request: Request, view: View) -> bool:
        if request.method == "DELETE" or request.method == "PATCH":
            return request.user.is_superuser
        else:
            return True
