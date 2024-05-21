"""
Purpose of the Course model is to store information about courses offered
within the main application.
"""

from django.db import models


class Course(models.Model):
    """
    Model representing the content/details of a course.
    """

    SEASON_CHOICES = [
        ("", "Select Season"),
        ("Spring", "Spring"),
        ("Summer", "Summer"),
        ("Autumn", "Autumn"),
    ]

    season = models.CharField(
        max_length=25,
        choices=SEASON_CHOICES,
        default="",
        blank=False,
        verbose_name="Season",
        help_text="Select the season during which the course is offered.",
    )

    title = models.CharField(
        max_length=255,
        verbose_name="Course Title",
        help_text="Enter the title of the course.",
    )

    date = models.DateField(
        verbose_name="Course Date",
        help_text="Enter the date on which the course is held.",
    )

    description = models.TextField(
        verbose_name="Course Description",
        help_text="Provide a detailed description of the course.",
    )

    location = models.CharField(
        max_length=255,
        verbose_name="Course Location",
        help_text="Enter the location where the course will take place.",
    )

    max_capacity = models.PositiveIntegerField(
        default=10,
        editable=False,
        verbose_name="Maximum Capacity",
        help_text="The maximum number of participants for the course.",
    )

    def __str__(self):
        return self.title
