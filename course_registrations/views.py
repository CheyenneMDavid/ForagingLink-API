"""
# This module defines the CourseRegistrations view and related functionalities.
# """

from rest_framework import generics, permissions
from .models import CourseRegistration
from .serializers import CourseRegistrationSerializer


class CourseRegistrationCreate(generics.CreateAPIView):
    """
    Inherits from "CreateAPIView"
    This view has no other purpose other than to create an instance for a User
    who is authenticated.
    """

    queryset = CourseRegistration.objects.all()
    serializer_class = CourseRegistrationSerializer
    # Access to creating a record is only available to authenticated users.
    permission_classes = [permissions.IsAuthenticated]


class CourseRegistrationDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    This inherits from "RetrieveUpdateDestroyAPIView" and as such is assigned
    the permission class of "IsAdmin" so that nobody else can make any changes
    to the CourseRegistrations
    """

    queryset = CourseRegistration.objects.all()
    serializer_class = CourseRegistrationSerializer
    # Permission to ensure a record can only be Read, Updated or Deleted by
    # someone who is an Admin.
    permission_classes = [permissions.IsAdminUser]
