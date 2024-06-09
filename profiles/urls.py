from django.urls import path
from profiles import views

"""
urls for the Profiles app.  Using namespaces to avoid conflicts with other
apps within the project
"""

app_name = "profiles"

urlpatterns = [
    path(
        "",
        views.ProfileList.as_view(),
        name="profile_list",
    ),
    path(
        "<int:pk>/",
        views.ProfileDetail.as_view(),
        name="profile_detail",
    ),
]
