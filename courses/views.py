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
from django.utils import timezone


# Assistance from StackOverflow pages here:
# https://stackoverflow.com/questions/9549744/
# django-correctly-retrieve-data-where-date-and-time-are-greater-than-now
# The code isn't copied but the understanding was grasped and tailored using
# the docs here: https://docs.djangoproject.com/en/5.0/topics/db/queries/
class CourseList(generics.ListAPIView):
    """
    View to retrieve instances in a read-only format.
    Inherits from "ListAPIView", allowing any user, authenticated or not, to
    read the content.

    The queryset is handled by a function that fetches instances of the
    courses, and filters them so they only include upcoming courses with dates
    that are greater than now, ordering them by date in ascending order, and
    limits the results to the top three.
    """

    serializer_class = CourseSerializer
    permission_classes = [AllowAny]

    def get_queryset(self):
        now = timezone.now()
        return Course.objects.filter(date__gt=now).order_by("date")[:3]

    """
    View to retrieve instances in a read-only format.
    Inherits from "ListAPIView", allowing any user, authenticated or not, to
    read the content.

    queryset is handled by a function that fetches instances of courses and
    filters them so that only the three newest are returned and that are
    listed in descending order
    """

    serializer_class = CourseSerializer
    permission_classes = [AllowAny]

    def get_queryset(self):
        now = timezone.now()
        return Course.objects.filter(date__gte=now).order_by("date")[:3]


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
