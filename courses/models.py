"""
This file defines the Course model and the fields within it.  It uses django's
built in validator, "MaxValueValidator" to manage the maximum places available
on a course.
"""

from django.core.validators import MaxValueValidator
from django.db import models


class Course(models.Model):
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
        validators=[MaxValueValidator(10)],
        verbose_name="Maximum Capacity",
        help_text="The maximum number of participants for the course.",
    )

    def __str__(self):
        return self.title
