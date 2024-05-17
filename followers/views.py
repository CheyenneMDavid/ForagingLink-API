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

    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Follower.objects.all()
    serializer_class = FollowerSerializer

    def perform_create(self, serializer):
        """
        Customizing the behavior of the "perform_create" method, associating
        the newly made Follower instance with the user making the request,
        and setting them as the owner.
        """

        serializer.save(owner=self.request.user)


class FollowerDetail(generics.RetrieveDestroyAPIView):
    """
    Inherits from "RetrieveDestroyAPIView" which provides the view with get,
    put, patch and delete method handlers.

    The permissions are set to "IsOwnerOrReadOnly", resulting in only the
    owner being able to creating a new instance when the follow another user.
    "all" in order to include all of the followers.
    """

    permission_classes = [IsOwnerOrReadOnly]
    queryset = Follower.objects.all()
    serializer_class = FollowerSerializer
