from django.urls import path
from plants_blog import views

"""
URLs for the Plants Blog app. Using namespaces to avoid conflicts with other
apps within the project.
"""

app_name = "plants_blog"

urlpatterns = [
    path(
        "",
        views.PlantInFocusPostList.as_view(),
        name="plant_posts",
    ),
    path(
        "create/",
        views.PlantInFocusPostCreate.as_view(),
        name="plant_post_create",
    ),
    path(
        "<int:pk>/",
        views.PlantInFocusPostDetail.as_view(),
        name="plant_post_detail",
    ),
]
