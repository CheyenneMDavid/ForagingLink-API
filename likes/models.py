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

    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    plant_in_focus_post = models.ForeignKey(
        PlantInFocusPost,
        related_name="likes",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )
    comment = models.ForeignKey(
        Comment,
        related_name="likes",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        """
        Instead of using "Unique_together", I'm using UniqueConstraint to
        enforce the owner of a like, only being able to like a comment or a
        post once, only, whilst also giving it a name, almost in the same way
        verbose names are used, enabling the pairing to be better understood.
        """

        constraints = [
            models.UniqueConstraint(
                fields=["owner", "plant_in_focus_post"],
                name="unique_like_per_post",
            ),
            models.UniqueConstraint(
                fields=["owner", "comment"], name="unique_like_per_comment"
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
