"""
This module defines the Course serializers and related functionalities.

"""

from rest_framework import serializers
from .models import Course


class CourseSerializer(serializers.ModelSerializer):
    """
    Serializer for the Course model.

    It's responsible for converting Course model data
    to and from JSON format.
    """

    class Meta:
        """
        Metadata for the CourseSerializer.  It specifies the fields
        to be serialized.
        """

        # Model to be serialised
        model = Course
        # Fields to be included in serializtion
        fields = [
            "id",
            "season",
            "title",
            "date",
            "description",
            "location",
            "max_capacity",
        ]
