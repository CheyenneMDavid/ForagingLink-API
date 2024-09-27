from django.urls import path
from followers import views

"""
urls for the Followers app.  Using namespaces to avoid conflicts with other
apps within the project
"""

# URL configurations for the followers app
# Using namespace for the followers app URL to avoid URL name clashes.
app_name = "followers"

urlpatterns = [
    path(
        "",
        # End point for listing all the followers
        views.FollowerList.as_view(),
        name="follower_list",
    ),
    path(
        # Endpoint for getting details of a specific follower using their ID
        "<int:pk>/",
        views.FollowerDetail.as_view(),
        name="follower_detail",
    ),
]
