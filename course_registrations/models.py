"""
CourseRegistration Model
It defines the CourseRegistration model for user registrations with necessary
fields to hold user information.
"""

from django.db import models
from django.contrib.auth.models import User
from courses.models import Course


STATUS_CHOICES = [
    ("Pending", "Pending"),
    ("Confirmed", "Confirmed"),
    ("Cancelled", "Cancelled"),
]


class CourseRegistration(models.Model):
    """
    This model represents a user's registration for a course and holds relevant
    data accordingly. The "status" field defaults to "Pending". This ensures
    courses aren't over-subscribed. It can be manually controlled via the
    admin panel.
    """

    course_title = models.ForeignKey(
        Course,
        default=3,
        on_delete=models.CASCADE,
        verbose_name="Course Title",
        help_text="The course this registration is for.",
    )
    owner = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name="Owner",
        help_text="The user this registration belongs to.",
    )
    email = models.EmailField(
        max_length=255,
        verbose_name="Email",
        help_text="The email address of the user.",
    )
    phone = models.CharField(
        max_length=20,
        verbose_name="Phone",
        help_text="The phone number of the user.",
    )
    registration_date = models.DateTimeField(
        auto_now=True,
        verbose_name="Registration Date",
        help_text="The date and time of registration.",
    )
    status = models.CharField(
        max_length=50,
        choices=STATUS_CHOICES,
        default="Pending",
        verbose_name="Status",
        help_text="The current status of the registration.",
    )
    dietary_restrictions = models.TextField(
        blank=True,
        null=True,
        verbose_name="Dietary Restrictions",
        help_text="Any dietary restrictions of the user.",
    )
    is_driver = models.BooleanField(
        default=False,
        verbose_name="Is Driver",
        help_text="Indicates if the user is a driver.",
    )
    ice_name = models.CharField(
        max_length=255,
        verbose_name="Emergency Contact Name",
        help_text="Name of the emergency contact person.",
    )
    ice_number = models.CharField(
        max_length=20,
        verbose_name="Emergency Contact Number",
        help_text="Phone number for the emergency contact, person.",
    )

    def __str__(self):
        return f"{self.owner.username}'s registration for: {self.course_title}"
