from django.urls import path
from likes import views

"""
urls for the Likes app.  Using namespaces to avoid conflicts with other
apps within the project
"""

app_name = "likes"

urlpatterns = [
    path(
        "",
        views.LikeList.as_view(),
        name="like_list",
    ),
    path(
        "<int:pk>/",
        views.LikeDetail.as_view(),
        name="like_detail",
    ),
]
