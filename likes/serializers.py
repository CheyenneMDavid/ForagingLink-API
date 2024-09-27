"""
This module defines the Likes serializers and related functionalities.

Much of the code in this file is copied from the drf-api walkthrough projects
with Code Institute.
"""

from django.db import IntegrityError
from rest_framework import serializers
from likes.models import Like
from plants_blog.models import PlantInFocusPost
from comments.models import Comment


class LikeSerializer(serializers.ModelSerializer):
    """
    Use of required=False applied to both plant_in_focus and comment, relying
    on the validate method to ensure that one of them is selcted.
    """

    # Read Only field for the user name of the likes's owner.
    owner = serializers.ReadOnlyField(source="owner.username")
    # Primary key related field for liking a specific plant post
    plant_in_focus_post = serializers.PrimaryKeyRelatedField(
        queryset=PlantInFocusPost.objects.all(), required=False
    )
    # Primary key related field for liking a specific comment
    comment = serializers.PrimaryKeyRelatedField(
        queryset=Comment.objects.all(), required=False
    )

    class Meta:
        """
        Meta class to map the Like model to the LikeSerializer and define the
        fields to be included.
        """

        # Model to be serialized
        model = Like
        # Fields to be included in serialization
        fields = [
            "id",
            "created_at",
            "owner",
            "plant_in_focus_post",
            "comment",
        ]

    def validate(self, data):
        """
        Raises a ValidationError to ensure that either plant_in_focus_post or
        comment is liked, but not both.
        """

        # If neither "plant_in_focus_post" or "comment" is provided, then
        # ValidationError is raised staing that one of them must be liked.
        if not data.get("plant_in_focus_post") and not data.get("comment"):
            raise serializers.ValidationError(
                "Either plant_in_focus_post or comment must be liked."
            )
        # If both the plant_in_focus_post and comment are provided, a
        # ValidationError is raised staing that only one can be liked.
        if data.get("plant_in_focus_post") and data.get("comment"):
            raise serializers.ValidationError(
                "Only one of plant_in_focus_post or comment can be liked."
            )
        # If one field is provided and the other is not, return the data
        # as valid.
        return data

    def create(self, validated_data):
        """
        Creates a new Like instance upon receiving valid data.
        Sets the owner of the Like to the user making the request.
        Raises a validation error if it's a duplicate.
        """
        # Assigns the current user as the owner of the like.
        validated_data["owner"] = self.context["request"].user
        try:
            # Attempts to create the Like instance
            return super().create(validated_data)
        except IntegrityError:
            # Raises a validation error if a duplicate is created.
            raise serializers.ValidationError(
                {"detail": "possible duplicate"}
            )
