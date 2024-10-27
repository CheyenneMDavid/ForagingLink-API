"""
This file has been predominantly copied from the DRF-API walkthrough project
with Code Institute.

It defines the user profile models and automatically creates a profile when a
new user is registered.
"""

from django.conf import settings
from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import User

# File level global variable for the default image to be used in the
# profiles application, with the prefix for Cloudinary's version caching,
# saving the job of updating the URL in the case of an alternative image were
# to be used as a default image.
DEFAULT_USER_AVATAR_PATH = (
    "v1730006283/foraging_link/user_avatars/default_avatar_fqwsjf.jpg"
)


class Profile(models.Model):
    """
    Represents a user profile and the fields within it.
    """

    # Owner has a one to one relationship with the User model.
    owner = models.OneToOneField(
        User,
        # Cascade used to the profile is deleted if the user is deleted.
        on_delete=models.CASCADE,
        verbose_name="Owner",
        help_text="The user this profile is for.",
    )
    # Automatically sets the date and time of when a profile is created.
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Created At",
        help_text="When the profile was created.",
    )
    # Automatically sets the date and time a profile is updated.
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name="Updated At",
        help_text="When the profile was last updated.",
    )
    # Stores the full name of the user, but can be left blank upon creation
    # and optionally filled out by user at a later date.
    name = models.CharField(
        max_length=255,
        blank=True,
        verbose_name="Name",
        help_text="The user’s full name.",
    )
    # Initially left blank upon creation, can be optionally filled ou by user
    # at a later date, providing chosen information about themselves.
    content = models.TextField(
        blank=True,
        verbose_name="Content",
        help_text="About the user.",
    )
    # Stores the user's profile image. Uses a default image if one isn't
    # uploaded
    image = models.ImageField(
        upload_to="foraging_link/user_avatars",
        default=DEFAULT_USER_AVATAR_PATH,
        verbose_name="Profile Image",
        help_text="Profile image of the user. Defaults to generic image if "
        "one is not provided",
    )

    @property
    def image_url(self):
        """
        Concatenates the global variable "CLOUDINARY_BASE_URL" from the
        "settings.py" which serves as a central point for access to images
        for allapplications and "DEFAULT_USER_AVATAR_PATH" defined at the of
        this file ensuring that the PEP8 79 character limit is maintained
        despite the long URLs for default images.
        """
        return f"{settings.CLOUDINARY_BASE_PATH}{DEFAULT_USER_AVATAR_PATH}"

    class Meta:
        """
        Meta class for the model.
        Ensuring that the most recent profiles are listed first
        """

        ordering = ["-created_at"]
        verbose_name = "Profile"
        verbose_name_plural = "Profiles"

    # Returns information about the owner of the profile.
    def __str__(self):
        return f"{self.owner}'s profile"


def create_profile(sender, instance, created, **kwargs):
    """
    Signal receiver function for creating a Profile instance automatically
    when a new User instance is created.
    """

    # Automatically creates a profile when a new user is registered.
    if created:
        Profile.objects.create(owner=instance)


post_save.connect(create_profile, sender=User)
