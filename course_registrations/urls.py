from django.urls import path
from course_registrations import views

"""
urls for the Course Registrations app.  Using namespaces to avoid conflicts 
with other apps within the project
"""

app_name = "course_registrations"

urlpatterns = [
    path(
        "create/",
        views.CourseRegistrationCreate.as_view(),
        name="courseregistration-create",
    ),
    path(
        "<int:pk>/",
        views.CourseRegistrationDetail.as_view(),
        name="courseregistration-detail",
    ),
]
