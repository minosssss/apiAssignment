from rest_framework import permissions
from rest_framework.permissions import BasePermission

from accountBook.models import Record


class IsOwner(BasePermission):

    def has_object_permission(self, request, view, obj):
        if request.user.is_authenticated:
            if request.user == obj.user:
                return True
            return False
        else:
            return False