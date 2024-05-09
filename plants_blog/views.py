"""
This file has been predominantly copied from the DRF-API walkthrough project
with Code Institute.

This file defines views for interacting with PlantInFocusPost entries.
It handles listing all entries and adding new ones with appropriate
permissions.
"""

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import PlantInFocusPost
from .serializers import PlantInFocusPostSerializer
from foraging_api.permissions import (
    IsAdminUserOrReadOnly,
)


class PlantInFocusPostList(APIView):
    """
    View for listing all PlantInFocusPosts and adding new posts.
    It allows authenticated users to view posts and only admin users to add
    new posts.
    """

    serializer_class = PlantInFocusPostSerializer
    permission_classes = [IsAdminUserOrReadOnly]

    def get(self, request):
        """
        Retrieves all plant focus posts and serializes them for JSON response.
        """
        plant_in_focus_posts = PlantInFocusPost.objects.all()
        serializer = self.serializer_class(
            plant_in_focus_posts, many=True, context={"request": request}
        )
        return Response(serializer.data)

    def post(self, request):
        """
        Allows only admin users to create a new post. If the post data
        is valid, it saves the post and returns it; otherwise, returns an
        error.
        """
        serializer = self.serializer_class(
            data=request.data, context={"request": request}
        )
        if serializer.is_valid():
            serializer.save(owner=request.user)
            return Response(
                serializer.data,
                status=status.HTTP_201_CREATED,
            )
        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST,
        )
