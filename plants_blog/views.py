"""
These views manage the retrieval, creation, and modification of
PlantInFocusPosts.
List View: Allows all users (authenticated or not) to browse posts.
Detail View: Allows all users (authenticated or not) to read the full posts.
but only admins can update or delete them.
Create View: Restricted to admin users only.
"""

from django.db.models import Count
from rest_framework import generics, filters
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

    serializer_class = PlantInFocusPostSerializer
    permission_classes = [AllowAny]
    queryset = PlantInFocusPost.objects.annotate(
        comments_count=Count("comments", distinct=True),
        likes_count=Count("likes", distinct=True),
    ).order_by("-created_at")

    filter_backends = [
        filters.OrderingFilter,
        filters.SearchFilter,
    ]

    ordering_fields = [
        "created_at",
        "main_plant_name",
        "comments_count",
    ]

    search_fields = [
        "main_plant_name",
        "main_plant_environment",
        "culinary_uses",
        "medicinal_uses",
        "history_and_folklore",
        "confusable_plant_name",
    ]


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

    queryset = PlantInFocusPost.objects.annotate(
        comments_count=Count("comments", distinct=True),
        likes_count=Count("likes", distinct=True),
    ).order_by("-created_at")

    serializer_class = PlantInFocusPostSerializer
    permission_classes = [IsAdminUserOrReadOnly]
