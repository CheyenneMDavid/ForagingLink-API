from django.urls import path
from course_registrations import views

"""
urls for the Course Registrations app.  Using namespaces to avoid conflicts 
with other apps within the project
"""

# URL configurations for the Course Registrations app

# Using namespace for the Course Registrations app URL to avoid URL name clashes.
app_name = "course_registrations"

urlpatterns = [
    path(
        # Endpoint for creating a registration
        "create/",
        views.CourseRegistrationCreate.as_view(),
        name="courseregistration_create",
    ),
    path(
        # Endpoint for handling an individual registration.
        "<int:pk>/",
        views.CourseRegistrationDetail.as_view(),
        name="courseregistration_detail",
    ),
]
