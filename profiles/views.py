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


class ProfileList(generics.ListAPIView):
    """
    View for listing all profiles. Retrieves all profiles from the database,
    annotates them with comments count, followers count, and following count,
    serializes them for JSON response, allowing for data to be easily handled
    on the client side.
    """

    queryset = Profile.objects.annotate(
        comments_count=Count("owner__comment", distinct=True),
        followers_count=Count("owner__followed", distinct=True),
        following_count=Count("owner__following", distinct=True),
    ).order_by("created_at")

    serializer_class = ProfileSerializer
    filter_backends = [filters.OrderingFilter]
    ordering_fields = [
        "comments_count",
        "followers_count",
        "following_count",
        "owner__followed__created_at",
        "owner__following__created_at",
    ]


class ProfileDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    View for retrieving detailed profile information. Annotates the profile
    with comments count, followers count, and following count, and serializes
    the data for JSON response. Allows only the owner of the profile to access
    the detailed information and facilities to update or delete their profile.
    """

    permission_classes = [IsOwnerOrReadOnly]
    queryset = Profile.objects.annotate(
        comments_count=Count("owner__comment", distinct=True),
        followers_count=Count("owner__followed", distinct=True),
        following_count=Count("owner__following", distinct=True),
    ).order_by("created_at")
    serializer_class = ProfileSerializer
