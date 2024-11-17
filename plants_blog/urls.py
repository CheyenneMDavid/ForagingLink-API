from django.urls import path
from plants_blog import views

"""
URLs for the Plants Blog API. Using namespaces to avoid conflicts with other
apps within the project.

The current paths are not utilized by the front end, as blog posts are
managed through the admin panel. These paths are included for future
development, where users with higher permissions than regular authenticated
users (but not necessarily full admins) will be able to access a screen to
create and edit blog posts.
"""

app_name = "plants_blog"

urlpatterns = [
    # URL for viewing the list of PlantInFocus posts.
    path(
        "posts/",
        views.PlantInFocusPostList.as_view(),
        name="plant_posts",
    ),
    # URL for creating a new PlantInFocus post (restricted to admins).
    path(
        "posts/create/",
        views.PlantInFocusPostCreate.as_view(),
        name="plant_post_create",
    ),
    # URL for viewing, updating, or deleting a specific PlantInFocus post.
    path(
        "posts/<int:pk>/",
        views.PlantInFocusPostDetail.as_view(),
        name="plant_post_detail",
    ),
]
