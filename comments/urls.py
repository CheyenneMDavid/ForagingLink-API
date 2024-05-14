"""
This module defines the URL patterns that are associated with the 
views in the comments app.

Much of the code in this file is copied from the drf-api walkthrough projects
with Code Institute.
"""

from django.urls import path
from comments import views

# URL patterns for post list views.
urlpatterns = [
    path("comments/", views.CommentList.as_view()),
    path("comments/<int:pk>/", views.CommentDetail.as_view()),
]
