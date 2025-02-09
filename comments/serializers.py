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
    to and from JSON format. Using 'naturaltime' for a more user-friendly
    format on the timestamps.
    """

    owner = serializers.ReadOnlyField(source="owner.username")
    is_owner = serializers.SerializerMethodField()
    profile_id = serializers.ReadOnlyField(source="owner.profile.id")
    profile_image = serializers.ReadOnlyField(
        source="owner.profile.image.url"
    )

    created_at = serializers.SerializerMethodField()
    updated_at = serializers.SerializerMethodField()
    replies = serializers.SerializerMethodField()

    replies_count = serializers.ReadOnlyField()
    likes_count = serializers.ReadOnlyField()
    like_id = serializers.SerializerMethodField()

    replying_comment = serializers.PrimaryKeyRelatedField(
        queryset=Comment.objects.all(),
        required=False,
        allow_null=True,
    )

    def validate_replying_comment(self, value):
        """
        Ensure that replies don't go more than 2 levels deep.
        """
        if value and value.replying_comment:
            raise serializers.ValidationError(
                "You can't reply to a comment that's already a reply."
            )

        return value

    def get_is_owner(self, obj):
        """
        Returns "True" if the requesting user is the owner of the comment.
        """
        return self.context["request"].user == obj.owner

    def get_like_id(self, obj):
        """
        Returns the like ID if the current user has liked the comment.
        """
        user = self.context["request"].user
        if user.is_authenticated:
            like = obj.likes.filter(owner=user).first()
            return like.id if like else None
        return None

    def get_created_at(self, obj):
        """
        Returns a user-friendly timestamp using "naturaltime".
        """
        return naturaltime(obj.created_at)

    def get_updated_at(self, obj):
        """
        Returns a user-friendly timestamp using "naturaltime".
        """
        return naturaltime(obj.updated_at)

    def get_replies(self, obj):
        """
        Returns serialized replies instead of just reply IDs.
        This allows full reply details to be included in the response
        rather than requiring an extra API call to fetch them.
        """
        return CommentSerializer(
            obj.replies.all(), many=True, read_only=True
        ).data

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
            "replying_comment",
            "likes_count",
            "like_id",
        ]


class CommentDetailSerializer(CommentSerializer):
    """
    Serializer for the Comment model, used in the Detail view context.

    Inherits from CommentSerializer and makes the 'plant_in_focus_post' field
    read-only to prevent changes in update operations.
    """

    plant_in_focus_post = serializers.ReadOnlyField(
        source="plant_in_focus_post.id"
    )
