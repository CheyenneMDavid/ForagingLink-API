"""
CourseRegistration Model
It defines the CourseRegistration model for user registrations with necessary
fields to hold user information.
"""

from django.db import models
from django.contrib.auth.models import User
from courses.models import Course

# Status of registrations selectable by the administrator form the admin panel
STATUS_CHOICES = [
    ("Pending", "Pending"),
    ("Confirmed", "Confirmed"),
    ("Cancelled", "Cancelled"),
]


class CourseRegistration(models.Model):
    """
    This model represents a user's registration for a course and holds
    relevant data accordingly. The "status" field defaults to "Pending". This
    ensures courses aren't over-subscribed. It can be manually controlled via
    the admin panel.
    """

    course_title = models.ForeignKey(
        Course,
        # Used a default value (3) to ensure smooth migrations when the
        # database lacked courses. Also acts as a support in case of all
        # courses being deleted.
        default=3,
        # CASCADE to delete the registration if the associated course is
        # deleted.
        on_delete=models.CASCADE,
        # Human friendly field name for the backend admin panel
        verbose_name="Course Title",
        # Help text for the admin to clarify what to input when they're
        # creating a registration
        help_text="Enter the title of the course for this registration.",
    )
    owner = models.ForeignKey(
        User,
        # CASCADE to delete the registration if the assosciated user is
        # deleted.
        on_delete=models.CASCADE,
        # Human friendly field name for the backend admin panel
        verbose_name="Owner",
        # Prompts the admin to select the user from the dropdown
        help_text="Select the user this registration belongs to.",
    )
    email = models.EmailField(
        max_length=255,
        # Human friendly field name for the backend admin panel
        verbose_name="Email",
        # Help text for the admin to prompt admin to input user email when
        # creating a registration
        help_text="The email address of the user.",
    )
    phone = models.CharField(
        # Limits the maximum length of the phone number
        max_length=20,
        # Human friendly field name for the backend admin panel
        verbose_name="Phone",
        # Prompts the admin to input the user's phone number
        help_text="The phone number of the user.",
    )
    registration_date = models.DateTimeField(
        # Automatically sets the registration date and time.
        auto_now=True,
        # Human friendly field name for the backend admin panel
        verbose_name="Registration Date",
        # Automatically inserts registration date
        help_text="The date and time of registration.",
    )
    status = models.CharField(
        max_length=50,
        choices=STATUS_CHOICES,
        default="Pending",
        # Human friendly field name for the backend admin panel
        verbose_name="Status",
        # Default status is set to 'Pending', which the admin can change.
        help_text="The current status of the registration.",
    )
    dietary_restrictions = models.TextField(
        blank=True,
        null=True,
        # Human friendly field name for the backend admin panel
        verbose_name="Dietary Restrictions",
        # Prompts admin to enter any food restrictions
        help_text="Any dietary restrictions of the user.",
    )
    is_driver = models.BooleanField(
        default=False,
        # Human friendly field name for the backend admin panel
        verbose_name="Is Driver",
        # Prompts admin to select whether the user is a driver
        help_text="Indicates if the user is a driver.",
    )
    ice_name = models.CharField(
        # Limits the maximum length of the emergency contact's name
        max_length=255,
        # Human friendly field name for the backend admin panel
        verbose_name="Emergency Contact Name",
        help_text="Name of the emergency contact person.",
    )
    ice_number = models.CharField(
        # Limits the maximum length of the emergency contact's phone number
        max_length=20,
        # Human friendly field name for the backend admin panel
        verbose_name="Emergency Contact Number",
        # Prompts admin to enter an emergency contact number
        help_text="Phone number for the emergency contact, person.",
    )

    def __str__(self):
        # String representation of the model, shows the username and course
        # title in admin interface.
        return (
            f"{self.owner.username}'s registration for: {self.course_title}"
        )
