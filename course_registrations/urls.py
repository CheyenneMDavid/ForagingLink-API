"""
This module defines the URL patterns that are associated with the views in
the course_registrations app.

Much of the code in this file is copied from the drf-api walkthrough projects
with Code Institute.
"""

from django.urls import path
from course_registrations import views

# URL patterns for post list views
urlpatterns = [
    path(
        "courseregistrations/create/",
        views.CourseRegistrationCreate.as_view(),
    ),
    path(
        "courseregistrations/<int:pk>/",
        views.CourseRegistrationDetail.as_view(),
    ),
]
