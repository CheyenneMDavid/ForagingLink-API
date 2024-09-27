"""
This module defines the Follower model and related functionalities.

Much of the code in this file is copied from the drf-api walkthrough projects
with Code Institute.
"""

from django.db import models
from django.contrib.auth.models import User


class Follower(models.Model):
    """
    Defining the Follower model, representing the relationship between users
    as followers of one another.
    """

    # "Owner" is the user that is doing the following.
    owner = models.ForeignKey(
        User,
        # If the user (owner/follower) is deleted, this follow relationship
        # will also be deleted.
        related_name="following",
        on_delete=models.CASCADE,
        verbose_name="Owner",
        help_text="The user who is following another user.",
    )

    # "Followed" is the user that is being followed by the owner.
    followed = models.ForeignKey(
        User,
        related_name="followed",
        # If the user (being followed) is deleted, this follow relationship
        # will also be deleted.
        on_delete=models.CASCADE,
        verbose_name="Followed",
        help_text="The user who is being followed.",
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Created At",
        help_text="Date and time when the follow relationship was created.",
    )

    class Meta:
        """
        Overriding the default behavior by listing followers, newest first.
        Using "unique_together" so users can't double up on following.
        """

        # Ensures orderin is most recent, first.
        ordering = ["-created_at"]
        # HELP and ADVICE
        # Using `unique_together`, courtesy of advice from StackOverflow
        # website, here: https://stackoverflow.com/questions/2201598
        # how-to-define-two-fields-unique-as-couple
        unique_together = [
            "owner",
            "followed",
        ]

    def __str__(self):
        return f"{self.owner} {self.followed}"
