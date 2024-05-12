"""
This file has been predominantly copied from the DRF-API walkthrough project
with Code Institute.

It defines views for interacting with profiles.
"""

from django.http import Http404
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Profile
from .serializers import ProfileSerializer
from foraging_api.permissions import IsOwnerOrReadOnly


class ProfileList(APIView):
    """
    View for listing all of the profiles. Retrieves all the profiles from the
    database, serializes them for JSON response, allowing for data to be
    easily handled on the client side.
    """

    def get(self, request):
        """
        Retrieves all profiles and serializes them. Uses 'many=True' in
        serializer
        to handle multiple objects.
        """
        profiles = Profile.objects.all()
        serializer = ProfileSerializer(
            profiles, many=True, context={"request": request}
        )
        return Response(serializer.data)


class ProfileDetail(APIView):
    """
    A view that handles HTTP requests for profile details.
    It utilizes the ProfileSerializer to handle serialization of profile data.
    """

    serializer_class = ProfileSerializer
    permission_classes = [IsOwnerOrReadOnly]

    def get_object(self, pk):
        """
        Attempts to retrieve a profile by its primary key (pk).
        If it exists, it is returned.
        If not found, it raises an HTTP 404 error.
        """
        try:
            profile = Profile.objects.get(pk=pk)
            self.check_object_permissions(self.request, profile)
            return profile
        except Profile.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        """
        Retrieves a profile using its primary key and serializes it to a format
        that can be easily converted to JSON for response.
        The serialized data is then sent back to the user.
        """
        profile = self.get_object(pk)
        serializer = ProfileSerializer(profile, context={"request": request})
        return Response(serializer.data)

    def put(self, request, pk):
        """
        Updates a profile identified by its primary key.
        The data from the request is used to update the profile. If the data
        is valid, the profile is saved.
        If the data is not valid, an HTTP 400 error is raised along with the
        error details.
        """
        profile = self.get_object(pk)
        serializer = ProfileSerializer(
            profile, data=request.data, context={"request": request}
        )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        """
        Deletes a profile identified by its primary key.
        """
        profile = self.get_object(pk)
        profile.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
