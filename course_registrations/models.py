"""
CourseRegistration Model
It defines the CourseRegistration model for user registrations with necessary
fields to hold user information.
"""

from django.db import models
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField
from django.core.validators import EmailValidator
from django.core.exceptions import ValidationError
from courses.models import Course

# Status of registrations selectable by the administrator form the admin panel
STATUS_CHOICES = [
    ("Confirmed", "Confirmed"),
    ("Cancelled", "Cancelled"),
]


class CourseRegistration(models.Model):
    """
    This model represents a user's registration for a course and stores all relevant data.
    The 'status' field defaults to 'Confirmed' and works in tandem with custom logic in the Course model to determine available spaces.

    If the status is changed to 'Cancelled' in the admin panel, the registration is
    excluded from space calculations, and the user's personal details are anonymized
    to retain minimal information for analytics without compromising privacy.

    Phone numbers are validated using the PhoneNumberField, based on
    regional standards, with the region set to "GB" (United Kingdom).

    The email field follows Django's standard 'max_length' recommendation
    to ensure compatibility with most systems. See Django's documentation
    for more information:
    https://docs.djangoproject.com/en/stable/ref/models/fields/#emailfield

    For more information on the "GB" code, refer to:
    https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2#GB

    Validation logic enforces completion of dietary restrictions and
    emergency contact fields, ensuring that details are provided if either
    option is selected.
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

    email = models.CharField(
        max_length=254,
        # The "validators" argument is passed to CharField(). It uses the
        # "EmailValidator()" to ensure the input is a valid email address.
        validators=[EmailValidator()],
        # Human friendly field name for the backend admin panel
        verbose_name="Email",
        # Help text for the admin to prompt admin to input user email when
        # creating a registration
        help_text="The email address of the user.",
    )

    phone = PhoneNumberField(
        # Region set to "GB"
        region="GB",
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
        default="Confirmed",
        verbose_name="Status",
        help_text="The current status of the registration.",
    )

    # Use of boolean field to define if the user has any dietary
    # restrictions, defaulting to False.
    has_dietary_restrictions = models.BooleanField(
        default=False,
        verbose_name="Has Dietary Restrictions",
        help_text="Indicates if the user has any dietary restrictions.",
    )
    # Text field to hold any dietary information if it exists.  Set to True,
    # but enforced by logic based on whether "has_dietary_restrictions" has
    # been ticked.
    dietary_restrictions = models.TextField(
        blank=True,
        null=True,
        # Human friendly field name for the backend admin panel
        verbose_name="Dietary Restrictions",
        # Prompts admin to enter any dietary restrictions if applicable.
        help_text="Details of the user's dietary restrictions, if any.",
    )

    is_driver = models.BooleanField(
        default=False,
        # Human friendly field name for the backend admin panel
        verbose_name="Is Driver",
        # Prompts admin to select whether the user is a driver
        help_text="Indicates if the user is a driver.",
    )

    # Boolean set to False. Asking if there is a person that can be contacted
    # in the case of an emergency. Selection between True or False, enforces t
    # he filling out of further details of 'ice_name' and
    # 'ice_number' (ICE full explanation:
    # https://en.wikipedia.org/wiki/In_Case_of_Emergency)
    has_emergency_contact = models.BooleanField(
        default=False,
        verbose_name="Has Emergency Contact",
        help_text="Tick if the user has an emergency contact.",
    )

    # "ICE" stands for "In Case of Emergency"
    ice_name = models.CharField(
        # Limits the maximum length of the emergency contact's name
        max_length=255,
        # Human friendly field name for the backend admin panel
        blank=True,  # explicitly set so django treats as such.
        null=True,  # explicitly set so django treats as such.
        verbose_name="Emergency Contact Name",
        help_text="Name of the emergency contact person.",
    )
    ice_number = PhoneNumberField(
        region="GB",
        # Human friendly field name for the backend admin panel
        blank=True,  # explicitly set so django treats as such.
        null=True,  # explicitly set so django treats as such.
        verbose_name="Emergency Contact Number",
        # Prompts admin to enter an emergency contact number
        help_text="Phone number for the emergency contact person.",
    )

    def clean(self):
        """
        Calling the "clean()" method to apply the custom validators based on
        the user's input:
        - If 'has_dietary_restrictions' is True, the 'dietary_restrictions'
        field must be filled.
        - If 'has_emergency_contact' is True, both 'ice_name' and
        'ice_number' must be provided.
        - If 'has_emergency_contact' is False, both 'ice_name' and
        'ice_number' must be left blank.
        """
        # Validate any dietary restrictions.
        if self.has_dietary_restrictions and not self.dietary_restrictions:
            raise ValidationError(
                "Please provide further details of any dietary restrictions."
            )

        # Validate any emergency contact information
        if self.has_emergency_contact:
            if not self.ice_name or not self.ice_number:
                raise ValidationError(
                    "Please provide both the emergency contact name and "
                    "number."
                )
        else:
            if self.ice_name or self.ice_number:
                raise ValidationError(
                    "Emergency contact name and number should be blank if"
                    "Has Emergency Contact' is unchecked."
                )

        # Superclass clean method called to ensure all previous validation is
        # applied before saving.
        super().clean()

    def anonymize(self):
        """
        Anonymize all the personal information when a registration is
        cancelled, making it suitable for keeping for analytical purposes.
        """
        self.email = "cancelled@example.com"
        self.phone = "0000000000"
        self.ice_name = "N/A"
        self.ice_number = "0000000000"

    def save(self, *args, **kwargs):
        # Check if status is set to "Cancelled" and anonymize if so
        if self.status == "Cancelled":
            self.anonymize()
        super().save(*args, **kwargs)

    def __str__(self):
        # String representation of the model, shows the username and course
        # title in admin interface.
        return (
            f"{self.owner.username}'s registration for: {self.course_title}"
        )
