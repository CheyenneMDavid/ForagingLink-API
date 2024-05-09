"""
This file has been adapted from the DRF-API walkthrough project
with Code Institute.

Defining custom permission classes to manage API access based on user ownership
and request methods.

"""

from rest_framework import permissions


class IsAdminUserOrReadOnly(permissions.BasePermission):
    """
    Custom permission that allows only admin users to perform editing
    operations,
    while allowing read operations for all authenticated users.
    """

    def has_permission(self, request, view):
        """
        Returns a "True" if permission is granted, and a "False" if
        permissions isn't granted.
        It allows authenticated users to read and only admins to write.
        """
        # Allow read-only access for any authenticated request
        if request.method in permissions.SAFE_METHODS:
            return request.user.is_authenticated
        # Write permissions require the user to be an admin
        return request.user.is_staff


class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Returns a "True" if permission is granted, and a "False" if permissions
    isn't granted.
    It allows authenticated users to read and only the owner of the object to
    write.
    """

    def has_object_permission(self, request, view, obj):
        # Allows read-only access for any authenticated request
        if request.method in permissions.SAFE_METHODS:
            return True
        # Write permissions require the user to be the owner.
        return obj.owner == request.user
