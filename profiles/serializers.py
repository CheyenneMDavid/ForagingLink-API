"""
This file has been predominantly copied from the DRF-API walkthrough project
with Code Institute.

Serializer for the Profile model, serializes Profile instances to and from 
JSON format.
"""

from rest_framework import serializers
from .models import Profile


class ProfileSerializer(serializers.ModelSerializer):
    """
    Serializes Profile instances to and from JSON format.
    """

    owner = serializers.ReadOnlyField(source="owner.username")
    is_owner = serializers.SerializerMethodField()

    def get_is_owner(self, obj):
        request = self.context["request"]
        return request.user == obj.owner

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
        ]
