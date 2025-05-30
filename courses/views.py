"""
This module defines the views for the Course model and related
functionalities.

The courses are readable by all users, whether they're authenticated or not,
and only admins can modify create or modify the content.
CourseList view allows anyone to read it.
CourseCreate and CourseUpdateDelete views only allow admins to change
anything.

The same effect could be achieved with fewer lines of code using
"ModelViewSet" due to its inheritance from "GenericAPIView", but separating
the views in this manner makes their individual roles more descriptive at a
glance.
"""

from rest_framework.permissions import AllowAny, IsAdminUser
from rest_framework import generics
from .models import Course
from .serializers import CourseSerializer
from django.utils import timezone
from foraging_api.permissions import IsAdminUserOrReadOnly


# Assistance from StackOverflow pages here:
# https://stackoverflow.com/questions/9549744/
# django-correctly-retrieve-data-where-date-and-time-are-greater-than-now
# The code isn't copied but the understanding was grasped and tailored using
# the docs here: https://docs.djangoproject.com/en/5.0/topics/db/queries/
class UpComingCourses(generics.ListAPIView):
    """
    View to retrieve instances in a read-only format.
    Inherits from "ListAPIView", allowing any user, authenticated or not, to
    read the content.

    The queryset is handled by a function that fetches instances of the
    courses, and filters them so they only include upcoming courses with dates
    that are greater than "now", ordering them by date in ascending order, and
    limits the results to the top three.
    """

    serializer_class = CourseSerializer
    permission_classes = [AllowAny]

    # Only fetches courses with dates set to future, and limits the return to
    # only 3 courses.
    def get_queryset(self):
        now = timezone.now()
        return Course.objects.filter(date__gt=now).order_by("date")[:3]


class FullCourseList(generics.ListAPIView):
    """
    View to retrieve instances in a read-only format.
    Inherits from "ListAPIView", allowing any user, authenticated or not, to
    read the content.
    FullCourseList returns all future courses, but unlik the "CourseList"
    view, it returns a complete list, making it available for the front end.
    """

    serializer_class = CourseSerializer
    permission_classes = [AllowAny]

    def get_queryset(self):
        now = timezone.now()
        return Course.objects.filter(date__gt=now).order_by("date")


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
    Inherits from "RetrieveUpdateDestroyAPIView" with "IsAdminUserOrReadOnly"
    permission class. It ensures that anyone can read course details, but
    only Admins can Update or Delete the course instances..
    """

    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    permission_classes = [IsAdminUserOrReadOnly]
