"""
This module defines the Comments view and related functionalities.

Much of the code in this file is copied from the drf-api walkthrough
project with Code Institute.
"""

from rest_framework import generics, permissions
from foraging_api.permissions import IsOwnerOrReadOnly
from .models import Follower
from .serializers import FollowerSerializer


class FollowerList(generics.ListCreateAPIView):
    """
    Inherits from ListCreateAPIView which provides get and post method
    handlers, which enables the view to list and create new instances.

    The permission is set to "IsAuthenticatedOrReadOnly" resulting in only
    Authenticated users being able to follow other users.

    "all" method to get the entire list of followers and have it ready for
    when it's needed.
    """

    # Only authenticated users can create followers.
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    # Queryset includes all Follower instances.
    queryset = Follower.objects.all()
    # Specifies the serializer used for representing the follower data.
    serializer_class = FollowerSerializer

    def perform_create(self, serializer):
        """
        Customizing the behavior of the "perform_create" method, associating
        the newly made Follower instance with the user making the request,
        and setting them as the owner.
        """

        # Saves the new Follower instance, defining the owner at the user
        # that is currently signed in.
        serializer.save(owner=self.request.user)


class FollowerDetail(generics.RetrieveDestroyAPIView):
    """
    Inherits from RetrieveDestroyAPIView, providing GET and DELETE method
    handlers to retrieve or delete a follower instance.
    The permissions are set to "IsOwnerOrReadOnly", so only the owner of the
    follower relationship can delete it, whilst anyone can view it.
    """

    # Only the owner can delete the follower instance, whilst anyone can view
    # it.
    permission_classes = [IsOwnerOrReadOnly]
    # Queryset includes all Follower instances.
    queryset = Follower.objects.all()
    # Specifies the serializer that's used for representing follower data.
    serializer_class = FollowerSerializer
