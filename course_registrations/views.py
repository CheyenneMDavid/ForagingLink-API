"""
This module defines the CourseRegistrations view and related functionalities.
"""

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
    permission_classes = [permissions.IsAuthenticated]


class CourseRegistrationDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    This inherits from "RetrieveUpdateDestroyAPIView" and as such is assigned
    the permission class of "IsAdmin" so that nobody else can make any changes
    to the CourseRegistrations
    """

    queryset = CourseRegistration.objects.all()
    serializer_class = CourseRegistrationSerializer
    permission_classes = [permissions.IsAdminUser]
