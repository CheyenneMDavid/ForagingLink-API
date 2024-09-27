from django.urls import path
from likes import views

"""
urls for the Likes app.  Using namespaces to avoid conflicts with other
apps within the project
"""

# Namespace for the Likes app to avoid URL conflicts with other apps.
app_name = "likes"

urlpatterns = [
    path(
        "",
        # URL pattern for the listing all likes and creating a like.
        views.LikeList.as_view(),
        name="like_list",
    ),
    path(
        # URL pattern for retrieving and deletion of a specific like by its ID
        "<int:pk>/",
        views.LikeDetail.as_view(),
        name="like_detail",
    ),
]
