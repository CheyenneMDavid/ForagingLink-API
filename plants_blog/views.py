"""
These views have been separated in this manner because I wanted all users,
whether authenticated or not, to be able to read a returned list of posts.
Initially, when using the Detail view, only authenticated users could read an
individual instance, which wasn't what I wanted. By separating the views, I
ensure that everyone can access both the list of posts, the details of
individual posts, and the search functionality, while still restricting the
ability to create, update, or delete posts to admin users.

Meanwhile, any comments that get added to posts have their own permissions set
in the `views.py` file within the comments app separately. This ensures that
only authenticated users can read the comments.
"""

from django.db.models import Count
from rest_framework import generics, filters
from .models import PlantInFocusPost
from .serializers import PlantInFocusPostSerializer
from rest_framework.permissions import AllowAny
from foraging_api.permissions import IsAdminUserOrReadOnly


# View to list all PlantInFocusPosts, allowing anyone to view the list.
class PlantInFocusPostList(generics.ListAPIView):
    """
    View for listing all PlantInFocusPosts.
    The posts are readable by all users, irrespective of whether they are
    authenticated or not.
    """

    serializer_class = PlantInFocusPostSerializer
    # Anyone can view the list of posts.
    permission_classes = [AllowAny]
    # Annotating the queryset with a distinct count of comments for each post
    # which can then be called forward and displayed in the front end.
    queryset = PlantInFocusPost.objects.annotate(
        # Using `distinct=True`` to ensure a single comment is only counted
        # the once.
        comments_count=Count("comment", distinct=True),
        likes_count=Count("likes", distinct=True),
    ).order_by("-created_at")

    # Filters for the search and ordering functionality in the backend.
    filter_backends = [
        filters.OrderingFilter,
        filters.SearchFilter,
    ]

    # Fields which can be used for the order.
    ordering_fields = [
        # Order by creation date
        "created_at",
        # Order by the plant's name
        "main_plant_name",
        # Order by the number of comments
        "comments_count",
    ]

    # Specifies the fields that are searchable.
    search_fields = [
        "main_plant_name",
        "main_plant_environment",
        "culinary_uses",
        "medicinal_uses",
        "history_and_folklore",
        "confusable_plant_name",
    ]


# View for creating PlantInFocusPosts, restricted to admins only.
class PlantInFocusPostCreate(generics.CreateAPIView):
    """
    View for creating new PlantInFocusPosts.
    It allows only the admin users to add new posts.
    """

    # Retrieves all PlantInFocus posts
    queryset = PlantInFocusPost.objects.all()
    # States the name of the seriealizer to be used
    serializer_class = PlantInFocusPostSerializer
    # Ensures that only an admin is able to create a post.
    permission_classes = [IsAdminUserOrReadOnly]

    # Assigns the current user as the owner of the post
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


# View for retrieving, updating, and deleting a specific PlantInFocusPost.
class PlantInFocusPostDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Handles retrieving, updating, and deleting a specific PlantInFocusPost.
    Allows any user to read the post details, but only admin users can update
    or delete posts.
    """

    # Fetches the post and includes a distinct count of comments.
    queryset = PlantInFocusPost.objects.annotate(
        comments_count=Count("comment", distinct=True),
        likes_count=Count("likes", distinct=True),
    ).order_by("-created_at")

    # Specifies serializer to be used.
    serializer_class = PlantInFocusPostSerializer
    # Detail of the post is readable by anyone, but the update and delete are
    # only available to an admin.
    permission_classes = [IsAdminUserOrReadOnly]
