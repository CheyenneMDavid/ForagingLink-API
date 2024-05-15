"""
This module defines the Likes serializers and related functionalities.

Much of the code in this file is copied from the drf-api walkthrough projects
with Code Institute.
"""

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
