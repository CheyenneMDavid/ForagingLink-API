"""
This file defines the Course model and the fields within it.  It uses django's
built in validator, "MaxValueValidator" to manage the maximum places available
on a course.
"""

from django.core.validators import MaxValueValidator
from django.db import models


# Choices for the seasons a course can be setup for from the admin panel.
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

    # Admins can choose titles of courses to allow for more flexability
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

    # Using Django's MaxValueValidator to ensure courses don't go over the
    # max capacity.
    max_capacity = models.PositiveIntegerField(
        default=10,
        validators=[MaxValueValidator(10)],
        verbose_name="Maximum Capacity",
        help_text="The maximum number of participants for the course.",
    )

    class Meta:
        # Courses to be displayed in admin panel, starting with most recent,
        # first.
        ordering = ["-date"]
        verbose_name = "Course"
        # Human readable plural name
        verbose_name_plural = "Courses"

    def __str__(self):
        """
        Returns the course title as a string representation for improved
        readability in the admin panel.
        """
        return self.title

    @property
    def available_spaces(self):
        """
        Calculates the number of available spaces based on "max_capacity"
        minus the current number of registrations. Returns a message if full.
        """
        # Get the count of registrations linked to this course
        confirmed_registrations = self.courseregistration_set.filter(
            status="Confirmed"
        ).count()

        # Calculate available spaces
        spaces_left = self.max_capacity - confirmed_registrations

        # Return a message if full, otherwise the number of spaces left
        return "No spaces available" if spaces_left == 0 else spaces_left
