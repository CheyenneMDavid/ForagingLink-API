"""
This module defines the Comment views and related functionalities.
It enables filtering and searching for comments whilst ensuring
proper permissions handling.

ListCreateAPIView: Allows listing and creating comments.
RetrieveUpdateDestroyAPIView: Allows viewing, updating, and deleting comments.
ListAPIView: Retrieves comment replies and comments by specific users.
"""

from django.db.models import Count
from rest_framework import generics, permissions, filters
from django_filters.rest_framework import DjangoFilterBackend
from foraging_api.permissions import IsOwnerOrReadOnly
from .models import Comment
from .serializers import CommentSerializer, CommentDetailSerializer


class CommentList(generics.ListCreateAPIView):
    """
    Lists all comments and allows authenticated users to create new comments.
    """

    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    queryset = Comment.objects.annotate(
        replies_count=Count("replies", distinct=True),
        likes_count=Count("likes", distinct=True),
    ).order_by("-created_at")

    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = [
        "plant_in_focus_post",
        "replying_comment",
        "owner__username",
    ]
    search_fields = [
        "content",
        "owner__username",
        "plant_in_focus_post__main_plant_name",
    ]

    def perform_create(self, serializer):
        """
        Assigns the current user as the owner of the comment.
        Ensures replies do not exceed two levels deep.
        """
        parent_comment = serializer.validated_data.get("replying_comment")
        if parent_comment:
            serializer.save(
                owner=self.request.user,
                plant_in_focus_post=parent_comment.plant_in_focus_post,
            )
        else:
            serializer.save(owner=self.request.user)


class CommentDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Allows a comment to be retrieved, updated, or deleted by its owner.
    """

    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = CommentDetailSerializer
    queryset = Comment.objects.annotate(
        replies_count=Count("replies", distinct=True),
        likes_count=Count("likes", distinct=True),
    ).order_by("-created_at")


class CommentReplyList(generics.ListAPIView):
    """
    Lists all replies to a specific comment.
    """

    serializer_class = CommentSerializer

    def get_queryset(self):
        """
        Returns replies associated with a specific comment.
        """
        parent_comment_id = self.kwargs["pk"]
        return Comment.objects.filter(replying_comment_id=parent_comment_id)


class CommentReplyDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Allows a reply to be retrieved, updated, or deleted by its owner.
    """

    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = CommentDetailSerializer

    def get_queryset(self):
        """
        Returns a specific reply to a comment based on primary keys.
        """
        parent_comment_id = self.kwargs["pk"]
        reply_id = self.kwargs["reply_pk"]
        return Comment.objects.filter(
            replying_comment_id=parent_comment_id, id=reply_id
        )


class ProfileCommentsList(generics.ListAPIView):
    """
    Lists all comments made by a specific user, allowing other authenticated
    users to see the comments made by a profile owner and their related posts.
    """

    serializer_class = CommentSerializer
    permission_classes = [permissions.AllowAny]

    def get_queryset(self):
        """
        Returns comments created by the user associated with the given profile ID.
        """
        profile_id = self.kwargs.get("profile_id")
        return Comment.objects.filter(owner__profile__id=profile_id).order_by(
            "-created_at"
        )
