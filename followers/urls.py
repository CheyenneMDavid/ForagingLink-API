from django.urls import path
from followers import views

"""
urls for the Followers app.  Using namespaces to avoid conflicts with other
apps within the project
"""

app_name = "followers"

urlpatterns = [
    path(
        "",
        views.FollowerList.as_view(),
        name="follower_list",
    ),
    path(
        "<int:pk>/",
        views.FollowerDetail.as_view(),
        name="follower_detail",
    ),
]
