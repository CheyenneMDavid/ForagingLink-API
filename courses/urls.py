from django.urls import path
from courses import views

"""
urls for the Courses app.  Using namespaces to avoid conflicts with other
apps within the project
"""

app_name = "courses"

urlpatterns = [
    path(
        "",
        views.CourseList.as_view(),
        name="course_list",
    ),
    path(
        "create/",
        views.CourseCreate.as_view(),
        name="course_create",
    ),
    path(
        "<int:pk>/",
        views.CourseUpdateDelete.as_view(),
        name="course_update_delete",
    ),
]
