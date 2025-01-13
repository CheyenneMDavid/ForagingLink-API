"""
This module defines the Like model, allowing users to like comments and
PlantInFocusPost instances separately or at the same time.
"""

from django.db import models
from django.contrib.auth.models import User


class Like(models.Model):
    """
    Represents a like by a user on a PlantInFocusPost or Comment.
    Each user can only like the same post or comment once.
    """

    owner = models.ForeignKey(
        User,
        on_delete=models.CASCADE,  # Deletes the like if the user is deleted.
        verbose_name="Owner",
        help_text="The user who likes the post or comment.",
    )

    plant_in_focus_post = models.ForeignKey(
        # Using a string reference in order to allow for lazy importing of the
        # PlantInFocusPost model.
        "plants_blog.PlantInFocusPost",
        related_name="likes",  # Enables reverse look up of likes on posts
        on_delete=models.CASCADE,  # Deletes likes if the post is deleted
        null=True,
        blank=True,  # Optional as like may be on post or a comment
        verbose_name="Plant in Focus Post",
    )

    comment = models.ForeignKey(
        # Using a string reference in order to allow for lazy importing of the
        # Comment model
        "comments.Comment",
        related_name="likes",  # Enables reverse look up of likes on comments.
        on_delete=models.CASCADE,  # Deletes likes if the comment is deleted
        null=True,
        blank=True,  # Optional as like may be on post or a comment
        verbose_name="Comment",
    )

    created_at = models.DateTimeField(
        auto_now_add=True,  # Automatically records the creation time.
        verbose_name="Created At",
    )

    class Meta:
        """
        Meta options for the Like model:
        - Enforces unique likes for each user on a post or comment.
        - Orders likes by creation time, newest first.
        """

        constraints = [
            models.UniqueConstraint(
                fields=["owner", "plant_in_focus_post"],
                name="unique_like_per_post",
            ),
            models.UniqueConstraint(
                fields=["owner", "comment"],
                name="unique_like_per_comment",
            ),
        ]
        ordering = ["-created_at"]

    def __str__(self):
        """
        Returns a string explaining who likes what.
        I'm using the + when concatenating the strings to get round the 79
        character limit.
        """
        if self.plant_in_focus_post:
            return (
                f"{self.owner.username} likes plant in focus post "
                + f"{self.plant_in_focus_post.id}"
            )
        elif self.comment:
            return f"{self.owner.username} likes comment {self.comment.id}"
