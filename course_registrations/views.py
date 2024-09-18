"""
This module defines the CourseRegistrations view and related functionalities.
"""

from rest_framework import generics, permissions
from .models import CourseRegistration
from .serializers import CourseRegistrationSerializer


class CourseRegistrationCreate(generics.CreateAPIView):
    """
    Allows authenticated users to create a course registration.
    """

    queryset = CourseRegistration.objects.all()
    serializer_class = CourseRegistrationSerializer
    permission_classes = [permissions.IsAuthenticated]


class CourseRegistrationDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Allows admin users to retrieve, update, or delete a course registration.
    """

    queryset = CourseRegistration.objects.all()
    serializer_class = CourseRegistrationSerializer
    permission_classes = [permissions.IsAdminUser]
