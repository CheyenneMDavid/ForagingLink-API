from django.urls import path
from courses import views

"""
urls for the Courses app.  Using namespaces to avoid conflicts with other
apps within the project
"""

# URL configurations for the courses app

# Using namespace for the courses app URLs to avoid URL name clashes.

app_name = "courses"

urlpatterns = [
    # Endpoint for listing all courses
    path(
        "",
        views.UpComingCourses.as_view(),
        name="up_coming_courses",
    ),
    path(
        # Endpoint for creation of courses, only available to admins
        "create/",
        views.CourseCreate.as_view(),
        name="course_create",
    ),
    path(
        # Endpoint for updating and deleting specific courses, only available
        # to admins.
        "<int:pk>/",
        views.CourseUpdateDelete.as_view(),
        name="course_update_delete",
    ),
    path(
        # Endpoint for the full list of courses.
        "full-list/",
        views.FullCourseList.as_view(),
        name="full_course_list",
    ),
]
