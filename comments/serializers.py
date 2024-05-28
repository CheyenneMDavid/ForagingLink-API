"""
This module defines the comments serializers and related functionalities.

Both the "CommentSerializer" and "CommentDetailSerializer" classes convert
comments to and from JSON format. Ownership of comments is checked for the
purpose of updating. Creation and updating are timestamped, while the
"naturaltime" function is used to provide timestamps in a more human-friendly
format.

Much of the code in this file is copied from the DRF-API walkthrough projects
with Code Institute.
"""

from django.contrib.humanize.templatetags.humanize import naturaltime
from rest_framework import serializers
from .models import Comment


class CommentSerializer(serializers.ModelSerializer):
    """
    Serializer for the Comment model handles the conversion of comments
    to and from JSON format.
    """

    owner = serializers.ReadOnlyField(source="owner.username")
    is_owner = serializers.SerializerMethodField()
    profile_id = serializers.ReadOnlyField(source="owner.profile.id")
    profile_image = serializers.ReadOnlyField(source="owner.profile.image.url")
    created_at = serializers.SerializerMethodField()
    updated_at = serializers.SerializerMethodField()
    replies = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    replies_count = serializers.ReadOnlyField()

    def get_is_owner(self, obj):
        """
        Returns "True" if the requesting user is the owner of the comment.
        """
        request = self.context["request"]
        return request.user == obj.owner

    def get_created_at(self, obj):
        """
        Returns time using "naturaltime" from Django's "humanize" module to
        display the timestamp in a more user-friendly way.
        """
        return naturaltime(obj.created_at)

    def get_updated_at(self, obj):
        """
        Returns time using "naturaltime" from Django's "humanize" module to
        display the timestamp in a more user-friendly way.
        """
        return naturaltime(obj.updated_at)

    class Meta:
        """
        Specifies the model to be used and the fields to be included.
        """

        model = Comment
        fields = [
            "id",
            "owner",
            "is_owner",
            "profile_id",
            "profile_image",
            "plant_in_focus_post",
            "created_at",
            "updated_at",
            "content",
            "replies",
            "replies_count",
        ]


class CommentDetailSerializer(CommentSerializer):
    """
    Serializer for the Comment model, used in the Detail view context.

    Inherits from CommentSerializer and makes the 'plant_in_focus_post' field
    read-only. This
    ensures that the associated post of a comment is not altered during update
    operations in the detail view.
    """

    plant_in_focus_post = serializers.ReadOnlyField(
        source="plant_in_focus_post.id",
    )
