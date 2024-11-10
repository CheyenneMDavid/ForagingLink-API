"""
This file has been predominantly copied from the DRF-API walkthrough project
with Code Institute.

It defines the user profile models and automatically creates a profile when a
new user is registered.
"""

from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import User


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
    # Stores the image used as user's avatar. Default image
    # is used if one isn't uploaded
    avatar = models.ImageField(
        upload_to="images/",
        default="default_avatar_pfb93f",
        verbose_name="Profile Image",
        help_text="Profile image of the user. Defaults to generic image "
        "if one is not provided",
        null=True,
        blank=True,
    )

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
