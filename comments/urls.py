from django.urls import path
from comments import views

"""
urls for the Comments app.  Using namespaces to avoid conflicts with other
apps within the project
"""

app_name = "comments"

urlpatterns = [
    path("", views.CommentList.as_view(), name="comment_list"),
    path("<int:pk>/", views.CommentDetail.as_view(), name="comment_detail"),
    path(
        "<int:pk>/replies/",
        views.CommentReplyList.as_view(),
        name="comment_replies",
    ),
    path(
        "<int:pk>/replies/<int:reply_pk>/",
        views.CommentReplyDetail.as_view(),
        name="comment_reply_detail",
    ),
]
