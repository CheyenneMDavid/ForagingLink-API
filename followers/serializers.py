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

        # Model to be serialized.
        model = Follower

        # List of all fields that will be included for serialization.
        fields = [
            "id",
            # User that follows another user.
            "owner",
            # Time stamp for when the following relationship is created.
            "created_at",
            # The user that is being followed.
            "followed",
            # Name of the user that's being followed
            "followed_name",
        ]

    def create(self, validated_data):
        """
        Tries to create a follower instance using valid data, raising error
        messages if unsuccessful.
        """
        try:
            # Calls the create method from serializers.ModelSerializer in
            # order to create a new follower instance
            return super().create(validated_data)
        except IntegrityError:
            # Returns a validation error if the follow relationship already
            # exists.
            raise serializers.ValidationError(
                {"detail": "possible duplicate"}
            )
