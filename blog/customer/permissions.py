from rest_framework.permissions import BasePermission


class ReadOnlyPermission(BasePermission):
    def has_permission(self, request, view):
        return True
        if request.method == "GET":
            return True

        if getattr(request.user, "is_authentificated", None):
            return True

        return False
