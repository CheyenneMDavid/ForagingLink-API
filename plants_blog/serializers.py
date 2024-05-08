"""
Serializer for the PlantInFocusPost model, serializes PlantInFocusPost
instances to and from JSON format.

"""

from rest_framework import serializers
from plants_blog.models import PlantInFocusPost


class PlantInFocusPostSerializer(serializers.ModelSerializer):
    """
    Serializes PlantInFocusPost instances to and from JSON format.
    """

    owner = serializers.ReadOnlyField(source="owner.username")

    class Meta:
        """
        Specifies the model and the fields that will be serialized.
        """

        model = PlantInFocusPost
        fields = [
            "id",
            "owner",
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
