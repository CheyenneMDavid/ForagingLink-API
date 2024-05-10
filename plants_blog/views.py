"""
This file has been predominantly copied from the DRF-API walkthrough project
with Code Institute.

This file defines views for interacting with PlantInFocusPost entries.
It handles listing all entries and adding new ones with appropriate
permissions.
"""

from django.http import Http404
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


class PlantInFocusPostDetail(APIView):
    """
    Handles Update, Deletion of specific PlantInFocusPost instances.

    Uses permissions ensure only admins can update or delete entries,
    whilst authenticated users can retrieve and read.
    """

    permission_classes = [IsAdminUserOrReadOnly]
    serializer_class = PlantInFocusPostSerializer

    def get_object(self, pk):
        """
        Retrieves a PlantInFocusPost object based on its primary key.
        And raises Http404 error if the object doesn't exist.
        """
        try:
            plant_in_focus_post = PlantInFocusPost.objects.get(pk=pk)
            self.check_object_permissions(
                self.request,
                plant_in_focus_post,
            )
            return plant_in_focus_post
        except PlantInFocusPost.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        """
        Handles the GET request to retrieve a specific PlantInFocusPost.
        """
        plant_in_focus_post = self.get_object(pk)
        serializer = PlantInFocusPostSerializer(
            plant_in_focus_post,
            context={"request": request},
        )
        return Response(serializer.data)

    def put(self, request, pk):
        """
        Handles the PUT request to update a specific PlantInFocusPost.
        """
        plant_in_focus_post = self.get_object(pk)
        serializer = PlantInFocusPostSerializer(
            plant_in_focus_post,
            data=request.data,
            context={
                "request": request,
            },
        )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        """
        Handles the DELETE request to remove a specific PlantInFocusPost.
        """
        plant_in_focus_post = self.get_object(pk)
        plant_in_focus_post.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
