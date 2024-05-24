"""drf_api URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include
from plants_blog.views import PlantInFocusPostList

"""
Main project's urls.py with patterns for the apps within it, using the 
PlantInFocusPost as the home page.
"""


urlpatterns = [
    path("", PlantInFocusPostList.as_view(), name="home"),
    path("admin/", admin.site.urls),
    path("api-auth/", include("rest_framework.urls")),
    path("profiles/", include("profiles.urls", namespace="profiles")),
    path("plants_blog/", include("plants_blog.urls", namespace="plants_blog")),
    path("comments/", include("comments.urls", namespace="comments")),
    path("likes/", include("likes.urls", namespace="likes")),
    path("followers/", include("followers.urls", namespace="followers")),
    path("courses/", include("courses.urls", namespace="courses")),
    path(
        "course_registrations/",
        include("course_registrations.urls", namespace="course_registrations"),
    ),
]
