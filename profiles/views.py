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


class ProfileList(generics.ListAPIView):
    """
    View for listing all profiles. Retrieves all profiles from the database,
    annotates them with comments count, followers count, and following count,
    serializes them for JSON response, allowing for data to be easily handled
    on the client side.
    Uses "IsAuthenticated" permission to restrict access to authenticated users
    only, ensuring unauthorized users cannot view the list of profiles.
    """

    queryset = Profile.objects.annotate(
        total_comments_count=Count("owner__comment", distinct=True),
        followers_count=Count("owner__followed", distinct=True),
        following_count=Count("owner__following", distinct=True),
    ).order_by("created_at")
    permission_classes = [IsAuthenticated]
    serializer_class = ProfileSerializer
    filter_backends = [filters.OrderingFilter]
    ordering_fields = [
        "total_comments_count",
        "followers_count",
        "following_count",
        "owner__followed__created_at",
        "owner__following__created_at",
    ]


class ProfileDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    View for retrieving detailed profile information. Annotates the profile
    with comments count, followers count, and following count, and serializes
    the data for JSON response.
    Uses "IsOwnerOrReadOnly" permission to allow only the owner of a profile to
    update or delete it. Additionally, utilizes "IsAuthenticated" permission to
    prevent unauthorized users from viewing profile details by adding an ID
    number onto the end of the profiles URL.
    """

    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]
    queryset = Profile.objects.annotate(
        total_comments_count=Count("owner__comment", distinct=True),
        followers_count=Count("owner__followed", distinct=True),
        following_count=Count("owner__following", distinct=True),
    ).order_by("created_at")
    serializer_class = ProfileSerializer
