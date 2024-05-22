"""
This module defines the views for the Course model and related functionalities.

The courses are readable by all users, whether they're authenticated or not,
and only admins can modify create or modify the content.
CourseList view allows anyone to read it.
CourseCreate and CourseUpdateDelete views only allow admins to change anything.

The same effect could be achieved with fewer lines of code using "ModelViewSet"
due to its inheritance from "GenericAPIView", but separating the views in this
manner makes their individual roles more descriptive at a glance.
"""

from rest_framework.permissions import AllowAny, IsAdminUser
from rest_framework import generics
from .models import Course
from .serializers import CourseSerializer


class CourseList(generics.ListAPIView):
    """
    View to retrieve instances in a read-only format.
    Inherits from "ListAPIView", allowing any user, authenticated or not, to
    read the content.
    """

    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    permission_classes = [AllowAny]


class CourseCreate(generics.CreateAPIView):
    """
    View to create new course instances.
    It inherits from "CreateAPIView" with "IsAdminUser" permission class,
    and ensures only Admins can create an instance.
    """

    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    permission_classes = [IsAdminUser]


class CourseUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
    """
    View to retrieve, update, or delete course instances.
    Inherits from "RetrieveUpdateDestroyAPIView" with "IsAdminUser" permission
    class. It ensures that only Admins can modify instances while allowing
    read-only access to course details.
    """

    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    permission_classes = [IsAdminUser]
