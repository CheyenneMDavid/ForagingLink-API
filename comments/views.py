"""
This module defines the Comment views and related functionalities.
It uses the DjangoFilterBackend to enable better filtering capabilities
in the API, allowing users to filter comments based on specific criteria.

The "ListCreateAPIView" is for listing and creating comments, with permissions
set to "IsAuthenticated", ensuring only authenticated users can view and
create comments. The "RetrieveUpdateDestroyAPIView" is used for retrieving,
updating, or deleting comments with permissions set to "IsOwnerOrReadOnly",
ensuring only the owners of comments can update or delete them.
Unauthenticated users cannot interact with comments unless
they sign up.

Much of the code in this file is copied from the DRF-API walkthrough
project with Code Institute and adapted for my own requirements.
"""

from django.db.models import Count
from rest_framework import generics, permissions, filters, serializers
from django_filters.rest_framework import DjangoFilterBackend
from foraging_api.permissions import IsOwnerOrReadOnly
from .models import Comment
from .serializers import CommentSerializer, CommentDetailSerializer


class CommentList(generics.ListCreateAPIView):
    """
    This view inherits from "ListCreateAPIView", a generic view for handling
    lists of objects. The permission class is set to "IsAuthenticated",
    allowing only authenticated users to view and create comments.
    """

    serializer_class = CommentSerializer
    # Ensures only authenticated users can interact with the comments
    permission_classes = [permissions.IsAuthenticated]
    queryset = Comment.objects.annotate(
        # Counts the number of replies each comment has.
        replies_count=Count("replies", distinct=True)
        # Orders comments starting with the newest first.
    ).order_by("-created_at")
    # Allows filtering and searching within the comments.
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = [
        # Enables filtering by the associated post.
        "plant_in_focus_post",
        # Enables filtering by the comment being replied to.
        "replying_comment",
        # Enables filtering by the username of the comment owner
        "owner__username",
    ]
    search_fields = [
        # Enables search according to the content of the comment.
        "content",
        # Enables filtering by the username of the comment owner
        "owner__username",
        # Enables search by the name of the plant in the post.
        "plant_in_focus_post__main_plant_name",
    ]

    def perform_create(self, serializer):
        """
        Creates a new comment.  It sets the currently logged in user as the
        owner of the comment

        If the comment is a reply to another comment, it ensures that replies are
        not nested beyond that level (i.e., replies to replies are not allowed).
        If a comment is attempted to be made as a reply to another reply (thus a second-level reply),
        a ValidationError is raised to maintain a simple and manageable discussion structure.
        Changed from previous use of ValueError to ValidationError to provide more specific feedback.
        """

        parent_comment = serializer.validated_data.get("replying_comment", None)
        if parent_comment and parent_comment.replying_comment:
            raise serializers.ValidationError(
                "You cannot reply to a reply beyond two levels."
            )
        # Assigns the logged-in user as the owner of the comment.
        serializer.save(owner=self.request.user)


class CommentDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Inherits from "RetrieveUpdateDestroyAPIView".
    Retrieves a comment, or updates or deletes it by id if you own it, using
    the permission "IsOwnerOrReadOnly".
    """

    # Using Generics to ensure that only the owner of the comment is able to edit or delete
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = CommentDetailSerializer
    queryset = Comment.objects.annotate(
        # Adds a reply count to each comment
        replies_count=Count("replies", distinct=True)
    ).order_by("-created_at")


class CommentReplyList(generics.ListAPIView):
    """
    View to list all replies to a specific comment.
    """

    serializer_class = CommentSerializer

    def get_queryset(self):
        """
        Return replies for the comment.
        """

        # Extracts comment ID (pk) from the URL
        parent_comment_id = self.kwargs["pk"]
        # Only returns the replies for the specific comment
        return Comment.objects.filter(replying_comment_id=parent_comment_id)


class CommentReplyDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    View to retrieve, update, or delete a specific reply to a comment.
    """

    # Using Generics to ensure that only the owner of the comment is able to edit or delete
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = CommentDetailSerializer

    def get_queryset(self):
        """
        Returns the specific reply for the given comment (pk) and reply (reply_pk).
        """

        # Primary Key for the parent coment.
        parent_comment_id = self.kwargs["pk"]
        # Primary Key for the reply comment.
        reply_id = self.kwargs["reply_pk"]
        return Comment.objects.filter(
            replying_comment_id=parent_comment_id, id=reply_id
        )
