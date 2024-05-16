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

    owner = models.ForeignKey(
        User,
        related_name="following",
        on_delete=models.CASCADE,
        verbose_name="Owner",
        help_text="The user who is following another user.",
    )
    followed = models.ForeignKey(
        User,
        related_name="followed",
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

        ordering = ["-created_at"]
        unique_together = [
            "owner",
            "followed",
        ]

    def __str__(self):
        return f"{self.owner} {self.followed}"
