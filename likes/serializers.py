"""
This module defines the Likes serializers and related functionalities.

Much of the code in this file is copied from the drf-api walkthrough projects
with Code Institute.
"""

from django.db import IntegrityError
from rest_framework import serializers
from likes.models import Like


class LikeSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source="owner.username")

    class Meta:
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
        Creates a new like instance upon receiving valid data.
        Raises an error if it's a duplicate.

        Changed to setting the owner of the Like to the user who's making the
        request. This way ensures that the owner field is already populated
        with the correct information before the Like instance is created in
        the database.  Less room errors.
        """
        validated_data["owner"] = self.context["request"].user
        try:
            return super().create(validated_data)
        except IntegrityError:
            raise serializers.ValidationError({"detail": "possible duplicate"})
