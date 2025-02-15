"""
This file has been predominantly copied from the DRF-API walkthrough project
with Code Institute.

Serializer for the Profile model, serializes Profile instances to and from
JSON format.
"""

from rest_framework import serializers
from .models import Profile
from followers.models import Follower


class ProfileSerializer(serializers.ModelSerializer):
    """
    Serializes Profile instances to and from JSON format.
    """

    owner = serializers.ReadOnlyField(source="owner.username")
    is_owner = serializers.SerializerMethodField()
    following_id = serializers.SerializerMethodField()
    total_comments_count = serializers.ReadOnlyField()
    followers_count = serializers.ReadOnlyField()
    following_count = serializers.ReadOnlyField()

    def get_is_owner(self, obj):
        request = self.context["request"]
        return request.user == obj.owner

    def get_following_id(self, obj):
        """
        Returns the ID of the 'Follower' object if the logged-in user follows
        the profile's owner. If not, it returns 'None'.
        """
        # Gets the currently logged-in user.
        user = self.context["request"].user
        # Checks if the user is authenticated.
        if user.is_authenticated:
            # Checks if the logged-in user follows the owner of this profile
            following = Follower.objects.filter(
                owner=user, followed=obj.owner
            ).first()

            # If a following relationship is found, return its ID; otherwise,
            # return None
            return following.id if following else None
        return None

    def validate_image(self, value):
        """
        Validates the image being used as an avatar's size and dimensions,
        raising a ValidationError message if the the image is outside the
        size and dimentions expected.
        """

        # Ensure that file size is not over 2MB
        if value.size > 2 * 1024 * 1024:
            raise serializers.ValidationError("Image size cannot exceed 2MB.")

        # Keeps image size to an expected size for an avatar without
        # compromising quality.
        if value.image.height > 512:
            raise serializers.ValidationError(
                "Image height cannot exceed 512 pixels."
            )

        # Keeps image size to an expected size for an avatar without
        # compromising quality.
        if value.image.width > 512:
            raise serializers.ValidationError(
                "Image width cannot exceed 512 pixels."
            )

        return value

    class Meta:
        """
        Specifies the model and fields that will be serialized.
        """

        model = Profile
        fields = [
            "id",
            "owner",
            "created_at",
            "updated_at",
            "name",
            "content",
            "image",
            "is_owner",
            "following_id",
            "total_comments_count",
            "followers_count",
            "following_count",
        ]
