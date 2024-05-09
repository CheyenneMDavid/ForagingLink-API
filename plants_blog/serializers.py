"""
Serializer for the PlantInFocusPost model, serializes PlantInFocusPost
instances to and from JSON format.

"""

from rest_framework import serializers
from plants_blog.models import PlantInFocusPost


class PlantInFocusPostSerializer(serializers.ModelSerializer):
    """
    Serializes PlantInFocusPost instances to and from JSON format.
    It includes image validation and returns ValidationError messages as
    strings that include the field_name in a string.
    """

    owner = serializers.ReadOnlyField(source="owner.username")
    is_owner = serializers.SerializerMethodField()
    profile_id = serializers.ReadOnlyField(source="owner.profile.id")
    profile_image = serializers.ReadOnlyField(source="owner.profile.image.url")

    def validate_image(self, value, field_name):
        if value.size > 2 * 1024 * 1024:
            raise serializers.ValidationError(
                f"{field_name} size cannot exceed 2MB.",
            )

        if value.image.height > 4096:
            raise serializers.ValidationError(
                f"{field_name} height cannot exceed 4096 pixels."
            )

        if value.image.width > 4096:
            raise serializers.ValidationError(
                f"{field_name} width cannot exceed 4096 pixels."
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
            "main_plant_environment",
            "culinary_uses",
            "medicinal_uses",
            "folklore",
            "main_plant_image",
            "confusable_plant_name",
            "confusable_plant_information",
            "confusable_plant_warnings",
            "confusable_plant_image",
        ]
