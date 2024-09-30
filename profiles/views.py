"""
This file has been predominantly copied from the DRF-API walkthrough project
with Code Institute.

It defines the views for interacting with profiles, including listing profiles
and retrieving detailed profile information with additional annotated fields.
"""

from django.db.models import Count
from rest_framework import generics, filters
from .models import Profile
from .serializers import ProfileSerializer
from foraging_api.permissions import IsOwnerOrReadOnly
from rest_framework.permissions import IsAuthenticated
from rest_framework.filters import SearchFilter


class ProfileList(generics.ListAPIView):
    """
    View for listing all profiles. Retrieves all profiles from the database,
    annotates them with comments count, followers count, and following count,
    and serializes them for JSON response. Profiles can be ordered by specific
    fields and searched by name or content, allowing easier handling on the
    client side. Uses "IsAuthenticated" permission to ensure only
    authenticated users can view the profiles.
    """

    # Gets all profiles and adds extra info like how many comments, followers,
    # and people the user is following.
    queryset = Profile.objects.annotate(
        # Counts how many comments the user has made
        total_comments_count=Count("owner__comment", distinct=True),
        # Counts how many followers the user has
        followers_count=Count("owner__followed", distinct=True),
        # Counts how many users, this user follows
        following_count=Count("owner__following", distinct=True),
        # Sorts profiles by the date they were created
    ).order_by("created_at")

    # Only logged-in users can view the profiles
    permission_classes = [IsAuthenticated]
    # Specifies name of the serializer to be used
    serializer_class = ProfileSerializer
    # Filters for ordering and searching
    filter_backends = [filters.OrderingFilter, SearchFilter]

    # Fields which can be used for the ordering the profiles
    ordering_fields = [
        "total_comments_count",
        "followers_count",
        "following_count",
        "owner__followed__created_at",
        "owner__following__created_at",
    ]

    # Fields that can be searched, such as user name and profile content
    search_fields = ["name", "content"]


class ProfileDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    View for retrieving detailed profile information. Annotates the profile
    with comments count, followers count, and following count, and serializes
    the data for JSON response. Only the profile owner can update or delete
    their profile. Uses "IsOwnerOrReadOnly" permission, along with
    "IsAuthenticated" to prevent unauthorized users from viewing or modifying
    profiles by ID.
    """

    # Only logged-in users can view, but only the owner can edit or delete
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]
    # Gets a specific profile with the aditional information of how many
    # comments, followers,

    queryset = Profile.objects.annotate(
        total_comments_count=Count("owner__comment", distinct=True),
        followers_count=Count("owner__followed", distinct=True),
        following_count=Count("owner__following", distinct=True),
    ).order_by("created_at")

    serializer_class = ProfileSerializer
