"""
This file has been predominantly copied from the DRF-API walkthrough project
with Code Institute.

Serializer for the PlantInFocus model, serializes PlantInFocus instances to
and from JSON format.
"""

from rest_framework import serializers
from plants_blog.models import PlantInFocusPost
from likes.models import Like


class PlantInFocusPostSerializer(serializers.ModelSerializer):
    """
    Serializes PlantInFocusPost instances to and from JSON format.
    It includes image validation and returns ValidationError messages as
    strings that include the image_field in a string.
    """

    owner = serializers.ReadOnlyField(source="owner.username")
    is_owner = serializers.SerializerMethodField()
    profile_id = serializers.ReadOnlyField(source="owner.profile.id")
    profile_image = serializers.ReadOnlyField(
        source="owner.profile.image.url"
    )
    like_id = serializers.SerializerMethodField()
    likes_count = serializers.ReadOnlyField()
    comments_count = serializers.ReadOnlyField()

    def validate_main_plant_parts_used(self, value):
        """
        Ensures "main_plant_parts_used" is not left as "Unknown" to prompt
        admins to provide a meaningful value.
        """
        if value == "Unknown":
            raise serializers.ValidationError(
                "You must specify the plant parts used, 'Unknown' is not"
                "allowed."
            )
        return value

    def get_is_owner(self, obj):
        """
        Returns True if the current request user is the owner of the object.
        """
        request = self.context.get("request", None)
        return request and request.user == obj.owner

    def get_like_id(self, obj):
        """
        Returns the ID of the Like object for the current user and the
        specified post, enabling toggling between like and unlike.
        """
        user = self.context["request"].user
        if user.is_authenticated:
            like = Like.objects.filter(
                owner=user, plant_in_focus_post=obj
            ).first()
            return like.id if like else None
        return None

    def validate_image(self, value, image_field):
        """
        Validates the image size and dimensions, replacing "image_field" with
        the actual field name in the error message.
        """
        if value.size > 2 * 1024 * 1024:
            raise serializers.ValidationError(
                f"{image_field} size cannot exceed 2MB.",
            )

        if value.image.height > 4096:
            raise serializers.ValidationError(
                f"{image_field} height cannot exceed 4096 pixels."
            )

        if value.image.width > 4096:
            raise serializers.ValidationError(
                f"{image_field} width cannot exceed 4096 pixels."
            )

        return value

    def validate_main_plant_image(self, value):
        return self.validate_image(value, "Main Plant Image")

    def validate_confusable_plant_image(self, value):
        return self.validate_image(value, "Confusable Plant Image")

    class Meta:
        """
        Specifies the model and the fields that will be serialized.
        """

        model = PlantInFocusPost

        fields = [
            "id",
            "owner",
            "is_owner",
            "profile_id",
            "profile_image",
            "created_at",
            "updated_at",
            "main_plant_name",
            "main_plant_month",
            "main_plant_environment",
            "culinary_uses",
            "medicinal_uses",
            "history_and_folklore",
            "main_plant_image",
            "main_plant_parts_used",
            "main_plant_warnings",
            "confusable_plant_name",
            "confusable_plant_information",
            "confusable_plant_warnings",
            "confusable_plant_image",
            "comments_count",
            "likes_count",
            "like_id",
        ]
