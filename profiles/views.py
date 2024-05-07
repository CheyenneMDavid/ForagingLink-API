"""
This file has been predominantly copied from the DRF-API walkthrough project
with Code Institute.

It defines views for interacting with profiles.
"""

from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Profile
from .serializers import ProfileSerializer


class ProfileList(APIView):
    """
    View for listing all of the profiles.
    """

    def get(self, request):
        """
        Retrieves all the profiles and serializes them.
        """
        profiles = Profile.objects.all()
        serializer = ProfileSerializer(profiles, many=True)
        return Response(serializer.data)
