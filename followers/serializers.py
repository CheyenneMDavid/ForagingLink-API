"""
This module defines the Followers serializers and related functionalities.

Much of the code in this file is copied from the drf-api walkthrough project
with Code Institute.
"""

from django.db import IntegrityError
from rest_framework import serializers
from .models import Follower


class FollowerSerializer(serializers.ModelSerializer):
    """
    Serializer class for the Follower model, including the Meta class that
    specifies the model to be serialized and the fields which are to be
    included in the serialized data.
    """

    owner = serializers.ReadOnlyField(source="owner.username")
    followed_name = serializers.ReadOnlyField(source="followed.username")

    class Meta:
        """
        Specifies the model associated with this serializer and the fields
        that need to be included in the serialized output
        """

        model = Follower

        fields = [
            "id",
            "owner",
            "created_at",
            "followed",
            "followed_name",
        ]

    def create(self, validated_data):
        """
        Tries to create a follower instance using valid data, raising error
        messages if unsuccessful.
        """
        try:
            return super().create(validated_data)
        except IntegrityError:
            raise serializers.ValidationError(
                {"detail": "possible duplicate"}
            )
