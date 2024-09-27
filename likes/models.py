"""
This module defines the Like model and related functionalities.

It allows the user to like both a comment and a plant_in_focus_post instance,
separately and also at the same time.
"""

from django.db import models
from django.contrib.auth.models import User
from comments.models import Comment
from plants_blog.models import PlantInFocusPost


class Like(models.Model):
    """
    Like model that can be linked to a Plant in focus post and also a Comment.
    Both posts and comments can be liked by the same user, but the user can
    only like each one of them, the once.
    """

    # Foreign key relationship to the User model to track who liked a post or
    # comment
    owner = models.ForeignKey(
        User,
        # Deletes the Like if the associated user is deleted
        on_delete=models.CASCADE,
        # Using verbose_name to create a more human like description of the
        # owner in the admin panel.
        verbose_name="Owner",
        # Using of help_text to provide context for the admin, in the admin
        # panel.
        help_text="The User who likes the post or comment.",
    )

    # Foreign key relationship to the PlantInFocusPost model to track which
    # post was liked
    plant_in_focus_post = models.ForeignKey(
        PlantInFocusPost,
        related_name="likes",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        verbose_name="Plant in Focus Post",
        help_text="The plant in focus post that's liked.",
    )
    comment = models.ForeignKey(
        Comment,
        related_name="likes",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        verbose_name="Comment",
        help_text="The comment that's liked.",
    )
    created_at = models.DateTimeField(
        # Timestamp for when the like is created, is generated autmatically.
        auto_now_add=True,
        verbose_name="Created At",
        help_text="The date and time when the like was created.",
    )

    class Meta:
        """
        Instead of using "Unique_together", I'm using UniqueConstraint to
        enforce the owner of a like, only being able to like a comment or a
        post once, only, whilst also giving it a name, almost in the same way
        verbose names are used, enabling the pairing to be better understood.
        """

        # Ensures an owner can only like a post or comment, once.
        constraints = [
            models.UniqueConstraint(
                fields=["owner", "plant_in_focus_post"],
                name="unique_like_per_post",
            ),
            models.UniqueConstraint(
                fields=["owner", "comment"], name="unique_like_per_comment"
            ),
        ]
        # Most recent listed first.
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
