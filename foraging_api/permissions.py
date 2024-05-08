"""
This file has been predominantly copied from the DRF-API walkthrough project
with Code Institute.

Defining custom permission classes to manage API access based on user ownership
and request methods.

"""

from rest_framework import permissions


class IsOwnerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.owner == request.user
