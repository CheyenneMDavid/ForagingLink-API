"""
These views have been separated in this manner because I wanted all users,
whether authenticated or not, to be able to read a returned list of posts.
Initially, when using the Detail view, only authenticated users could read an
individual instance, which wasn't what I wanted. By separating the views, I
ensure that everyone can access both the list of posts and the details of
individual posts, while still restricting the ability to create, update, or
delete posts to admin users.

Meanwhile, any comments that get added to posts have their own permissions set
in the `views.py` file within the comments app separately. This ensures that
only authenticated users can read the comments.
"""

from rest_framework import generics
from .models import PlantInFocusPost
from .serializers import PlantInFocusPostSerializer
from rest_framework.permissions import AllowAny
from foraging_api.permissions import IsAdminUserOrReadOnly


class PlantInFocusPostList(generics.ListAPIView):
    """
    View for listing all PlantInFocusPosts.
    The posts are readable by all users, irrespective of whether they are
    authenticated or not.
    """

    queryset = PlantInFocusPost.objects.all()
    serializer_class = PlantInFocusPostSerializer
    permission_classes = [AllowAny]


class PlantInFocusPostCreate(generics.CreateAPIView):
    """
    View for creating new PlantInFocusPosts.
    It allows only the admin users to add new posts.
    """

    queryset = PlantInFocusPost.objects.all()
    serializer_class = PlantInFocusPostSerializer
    permission_classes = [IsAdminUserOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class PlantInFocusPostDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Handles retrieving, updating, and deleting a specific PlantInFocusPost.
    Allows any user to read the post details, but only admin users can update
    or delete posts.
    """

    queryset = PlantInFocusPost.objects.all()
    serializer_class = PlantInFocusPostSerializer

    def get_permissions(self):
        if self.request.method in ["GET", "HEAD", "OPTIONS"]:
            return [AllowAny()]
        return [IsAdminUserOrReadOnly()]
