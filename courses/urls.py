"""
This module defines the URL patterns that are associated with the views in
the courses app.

Much of the code in this file is copied from the drf-api walkthrough projects
with Code Institute.
"""

from django.urls import path
from courses import views

urlpatterns = [
    path("courses/", views.CourseList.as_view()),
    path("courses/create/", views.CourseCreate.as_view()),
    path("courses/<int:pk>/", views.CourseUpdateDelete.as_view()),
]
