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

    queryset = Like.objects.all()
    serializer_class = LikeSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ["owner", "plant_in_focus_post", "comment"]


class LikeDetail(generics.RetrieveDestroyAPIView):
    """
    Inherits from RetrieveDestroyAPIView which gives it method handlers to
    retrieve and destroy likes.
    By using the IsOwnerOrReadOnly permission class, only the owner of the
    like can delete it.
    """

    queryset = Like.objects.all()
    serializer_class = LikeSerializer
    permission_classes = [IsOwnerOrReadOnly]
