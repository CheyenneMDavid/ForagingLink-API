"""
This module defines the Course serializers and related functionalities.

"""

from rest_framework import serializers
from .models import Course


class CourseSerializer(serializers.ModelSerializer):
    """
    Serializer for the Course model.

    It includes a field called 'available_spaces'. It's not saved in the
    database, but is worked out when the data is sent to the frontend.
    It shows how many places are left by taking the course's max size and
    subtracting the number of confirmed bookings.
    """

    available_spaces = serializers.SerializerMethodField()

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
            "available_spaces",
        ]

    def get_available_spaces(self, obj):
        return obj.available_spaces
