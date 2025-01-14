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
        help_text="The user following another user.",
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
        Using UniqueConstraint so users can't double up on following.
        Changes from using `unique_together` due to depreciation and
        replacement by `UniqueConstraints` as explained in
        https://django.readthedocs.io/en/stable/ref/models/options.html,
        under the section of unique_together - Options.unique_together
        """

    # Ensures ordering is most recent, first.
    ordering = ["-created_at"]

    # Use of UniqueConstraint to enforce that a user can't follow the same
    # user twice.
    constraints = [
        models.UniqueConstraint(
            fields=["owner", "followed"], name="unique_following"
        )
    ]

    def __str__(self):
        return f"{self.owner} {self.followed}"
