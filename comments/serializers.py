"""
This module defines the comments serializers and related functionalities.

Much of the code in this file is copied from the drf-api walkthrough projects
with Code Institute.
"""

from django.contrib.humanize.templatetags.humanize import naturaltime
from rest_framework import serializers
from .models import Comment


class CommentSerializer(serializers.ModelSerializer):
    """
    Serializer for the Comment model handling the conversion of comments,
    to and from JSON format.
    """

    # Read-only field to get the username of the comment owner.
    owner = serializers.ReadOnlyField(source="owner.username")

    # Method field determines if the current request user is the owner of the
    # comment.
    is_owner = serializers.SerializerMethodField()

    # Read-only fields getting profile-related information of the comment
    # owner.
    profile_id = serializers.ReadOnlyField(source="owner.profile.id")
    profile_image = serializers.ReadOnlyField(source="owner.profile.image.url")
    created_at = serializers.SerializerMethodField()
    updated_at = serializers.SerializerMethodField()
    # Facilitates commenting on comments.
    replies = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    def get_is_owner(self, obj):
        """
        Returns "True" if the requesting user is the owner of the
        post. If they're not, it returns a "False"
        """
        request = self.context["request"]
        return request.user == obj.owner

    def get_created_at(self, obj):
        """
        Returns time using "naturaltime" from Django's "humanize module" to
        display timestamp in a more user friendly way.
        """
        return naturaltime(obj.created_at)

    def get_updated_at(self, obj):
        """
        Returns time using "naturaltime" from Django's "humanize module" to
        display timestamp in a more user friendly way.
        """
        return naturaltime(obj.updated_at)

    class Meta:
        """
        Specifies the model to be used and says which fields will be
        included
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
        ]


class CommentDetailSerializer(CommentSerializer):
    """
    Serializer for the Comment model, used in the Detail view
    context.

    Inherits from CommentSerializer and makes the post field read-only. This
    ensures
    that the associated post of a comment is not altered during update
    operations in
    the detail view.
    """

    # The 'post' field is read-only to prevent changing the associated post
    # during updates.

    # Displays only the ID of the associated post for clarity and efficiency.
    plant_in_focus_post = serializers.ReadOnlyField(
        source="plant_in_focus_post.id",
    )
