"""
This module defines the Likes serializers and related functionalities.

Much of the code in this file is copied from the drf-api walkthrough projects
with Code Institute.
"""

from django.db import IntegrityError
from rest_framework import serializers
from likes.models import Like


class LikeSerializer(serializers.ModelSerializer):
    """
    Serializer for the Like model.

    This serializer is responsible for converting Like model instances
    into JSON format and vice versa for use in API views.
    """

    owner = serializers.ReadOnlyField(source="owner.username")

    class Meta:
        """
        Stating that it's the Like model that is to be serialized.
        States the fields that need to be included.
        """

        model = Like
        fields = [
            "id",
            "created_at",
            "owner",
            "plant_in_focus_post",
            "comment",
        ]

    def create(self, validated_data):
        """
        Creates a new like instance upon receiving valid data and raises an
        error if it's been duplicated.
        """
        try:
            return super().create(validated_data)
        except IntegrityError:
            raise serializers.ValidationError({"detail": "possible duplicate"})
