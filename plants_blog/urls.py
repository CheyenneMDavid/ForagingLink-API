from django.urls import path
from plants_blog import views

"""
URLs for the Plants Blog app. Using namespaces to avoid conflicts with other
apps within the project.
"""

app_name = "plants_blog"

urlpatterns = [
    path(
        # URL for viewing the list of PlantInFocus posts.
        "",
        views.PlantInFocusPostList.as_view(),
        name="plant_posts",
    ),
    path(
        # URL for creating a new PlantInFocus post (restricted to admins).
        "create/",
        views.PlantInFocusPostCreate.as_view(),
        name="plant_post_create",
    ),
    path(
        # URL for viewing, updating, or deleting a specific PlantInFocus post.
        "<int:pk>/",
        views.PlantInFocusPostDetail.as_view(),
        name="plant_post_detail",
    ),
]
