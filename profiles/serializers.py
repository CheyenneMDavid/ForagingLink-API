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

    def get_is_owner(self, obj):
        request = self.context["request"]
        return request.user == obj.owner

    def get_following_id(self, obj):
        user = self.context["request"].user
        if user.is_authenticated:
            following = Follower.objects.filter(
                owner=user,
                followed=obj.owner,
            ).first()
            print(following)
            return following.id if following else None
        return None

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
        ]
