from django.urls import path
from comments import views

"""
urls for the Comments app.  Using namespaces to avoid conflicts with other
apps within the project
"""

# URL configurations for the comments app

# Using namespace for the comments app URL to avoid URL name clashes.
app_name = "comments"

urlpatterns = [
    # Endpoint for listing and creating comments.
    path("", views.CommentList.as_view(), name="comment_list"),
    # Endpoint for handling individual comments.
    path("<int:pk>/", views.CommentDetail.as_view(), name="comment_detail"),
    # Endpoint for listing replies to a comment.
    path(
        "<int:pk>/replies/",
        views.CommentReplyList.as_view(),
        name="comment_replies",
    ),
    # Endpoint for handling individual replies.
    path(
        "<int:pk>/replies/<int:reply_pk>/",
        views.CommentReplyDetail.as_view(),
        name="comment_reply_detail",
    ),
]
