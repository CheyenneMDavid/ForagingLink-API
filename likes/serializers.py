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
    owner = serializers.ReadOnlyField(source="owner.username")
    plant_in_focus_post = serializers.PrimaryKeyRelatedField(
        queryset=PlantInFocusPost.objects.all(), required=False
    )
    comment = serializers.PrimaryKeyRelatedField(
        queryset=Comment.objects.all(), required=False
    )

    class Meta:
        """
        Meta class to map the Like model to the LikeSerializer and define the
        fields to be included.
        """

        model = Like
        fields = [
            "id",
            "created_at",
            "owner",
            "plant_in_focus_post",
            "comment",
        ]

    def validate(self, data):
        """
        Ensures that a plant_in_focus_post or comment is liked, but not both
        as a result of the same instance that's created.
        """
        if not data.get("plant_in_focus_post") and not data.get("comment"):
            raise serializers.ValidationError(
                "Either plant_in_focus_post or comment must be liked."
            )
        if data.get("plant_in_focus_post") and data.get("comment"):
            raise serializers.ValidationError(
                "Only one of plant_in_focus_post or comment can be liked."
            )
        return data

    def create(self, validated_data):
        """
        Creates a new Like instance upon receiving valid data.
        Sets the owner of the Like to the user making the request.
        Raises a validation error if it's a duplicate.
        """
        validated_data["owner"] = self.context["request"].user
        try:
            return super().create(validated_data)
        except IntegrityError:
            raise serializers.ValidationError({"detail": "possible duplicate"})
