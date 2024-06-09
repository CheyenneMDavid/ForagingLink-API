from django.urls import path
from comments import views

"""
urls for the Comments app.  Using namespaces to avoid conflicts with other
apps within the project
"""

app_name = "comments"

urlpatterns = [
    path(
        "",
        views.CommentList.as_view(),
        name="comment_list",
    ),
    path(
        "<int:pk>/",
        views.CommentDetail.as_view(),
        name="comment_detail",
    ),
]
