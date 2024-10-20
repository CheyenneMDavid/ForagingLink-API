"""
This module defines the Likes view and related functionalities.

Much of the code in this file is copied and adapted from the drf-api
walkthrough
project with Code Institute.
"""

from rest_framework import generics, permissions
from django_filters.rest_framework import DjangoFilterBackend
from likes.models import Like
from likes.serializers import LikeSerializer
from foraging_api.permissions import IsOwnerOrReadOnly


class LikeList(generics.ListCreateAPIView):
    """
    Inherits from ListCreateAPIView which allows it to read and write.
    IsAuthenticatedOrReadOnly allows all users to see likes but only
    authenticated users are able to like.
    """

    # Queryset that returns all Like objects
    queryset = Like.objects.all()

    # Serializer handing the likes objects that are returned.
    serializer_class = LikeSerializer
    # Read Only access to unauthenticated users, whilst authenticated can
    # create a like.
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    # Backend handling the filtering of querysets
    filter_backends = [DjangoFilterBackend]
    # Specific fields that are used for filtering requests.
    filterset_fields = [
        "owner",
        "plant_in_focus_post",
        "comment",
    ]


class LikeDetail(generics.RetrieveDestroyAPIView):
    """
    Inherits from RetrieveDestroyAPIView which gives it method handlers to
    retrieve and destroy likes.
    By using the IsOwnerOrReadOnly permission class, only the owner of the
    like can delete it.
    """

    # Queryset that returns all Like objects
    queryset = Like.objects.all()
    # Serializer to handle Like objects
    serializer_class = LikeSerializer
    # Only owners of a like object are able to destroy it.
    permission_classes = [IsOwnerOrReadOnly]
