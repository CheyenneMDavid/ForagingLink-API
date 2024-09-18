"""
This module defines the CourseRegistrations serializers and related
functionalities.

"""

from rest_framework import serializers
from .models import CourseRegistration


class CourseRegistrationSerializer(serializers.ModelSerializer):
    """
    Serializer for the "CourseRegistration" model.

    It's responsible for converting CourseRegistration model data
    to and from JSON format.
    """

    class Meta:
        """
        Specifies the model to be used and says which fields will be
        included
        """

        # Specifies the model to serialized
        model = CourseRegistration
        # List of fields to be included
        fields = [
            "id",
            "course_title",
            "owner",
            "email",
            "phone",
            "registration_date",
            "status",
            "dietary_restrictions",
            "is_driver",
            "ice_name",
            "ice_number",
        ]
