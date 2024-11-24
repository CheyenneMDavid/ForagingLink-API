"""
This file has been predominantly copied from the DRF-API walkthrough project
with Code Institute.

Serializer for the PlantInFocus model, serializes PlantInFocus instances to
and from JSON format.
"""

from rest_framework import serializers
from plants_blog.models import PlantInFocusPost


class PlantInFocusPostSerializer(serializers.ModelSerializer):
    """
    Serializes PlantInFocusPost instances to and from JSON format.
    It includes image validation and returns ValidationError messages as
    strings that include the image_field in a string.
    """

    # Read-only field returning the owner's username
    owner = serializers.ReadOnlyField(source="owner.username")
    # Checks if the current user is the post owner.
    is_owner = serializers.SerializerMethodField()
    # Returns owner's profile ID
    profile_id = serializers.ReadOnlyField(source="owner.profile.id")
    # Returns the URL for the owner's profile image.
    profile_image = serializers.ReadOnlyField(
        source="owner.profile.image.url"
    )
    # Returns the count for comments on the post.
    comments_count = serializers.ReadOnlyField()

    # Custom field validation for 'main_plant_parts_used'
    def validate_main_plant_parts_used(self, value):
        """
        Validates the "main_plant_parts_used" field, ensuring the field isn't
        left with the default value of "Unknown", prompting the admins who
        create the post to provide a more meaningful value.
        If the field isn't changed from "Unknown", a ValidationError is
        raised.
        """
        if value == "Unknown":
            raise serializers.ValidationError(
                "You must specify the plant parts used, 'Unknown' is not"
                "allowed."
            )
        return value

    # Method to check if the currently logged in user is the owner of the post
    def get_is_owner(self, obj):
        """
        Returns True if the current request user is the owner of the object.
        """
        request = self.context.get("request", None)
        return request and request.user == obj.owner

    def validate_image(self, value, image_field):
        """
        Validates the image size and dimensions, using "image_field" as a
        placeholder in ValidationErrors, dynamically replaced by the actual
        field name in the error message.
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

    # Validates the main plant image.
    def validate_main_plant_image(self, value):
        return self.validate_image(value, "Main Plant Image")

    # Validates the confusable plant image.
    def validate_confusable_plant_image(self, value):
        return self.validate_image(value, "Confusable Plant Image")

    class Meta:
        """
        Specifies the model and the fields that will be serialized.
        """

        # Specifies the model to be serialized
        model = PlantInFocusPost
        # Specifies the fields to be included in the searialization
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
        ]
