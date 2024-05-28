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
from rest_framework import generics, permissions, filters
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
    permission_classes = [permissions.IsAuthenticated]
    queryset = Comment.objects.annotate(
        replies_count=Count("replies", distinct=True)
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
        Creates a new comment and associates it with the logged-in user.

        This method is called when creating a new comment and ensures
        that the comment is associated with the user who is currently logged
        in.
        """
        serializer.save(owner=self.request.user)


class CommentDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Inherits from "RetrieveUpdateDestroyAPIView".
    Retrieves a comment, or updates or deletes it by id if you own it, using
    the permission "IsOwnerOrReadOnly".
    """

    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = CommentDetailSerializer
    queryset = Comment.objects.annotate(
        replies_count=Count("replies", distinct=True)
    ).order_by("-created_at")
