"""
This module defines the Comments model and related functionalities.

For much of the code in this file, I've used the drf-api walkthrough projects
with Code Institute as a guide.
"""

from django.db import models
from django.contrib.auth.models import User
from plants_blog.models import PlantInFocusPost


class Comment(models.Model):
    """
    Comments are associated with the User who made the comment and the
    posts that the comments are on.

    Using SET_NULL to retain comments when an author deletes their account,
    setting the username to 'inactive user'.

    If the `plant_in_focus_post` itself is deleted, the associated comments
    are also deleted using CASCADE.

    Using "replying_comment" as a foreign key to allow comments to be replies
    to other comments.
    """

    owner = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        verbose_name="Owner",
        help_text="The user who made the comment.",
    )

    plant_in_focus_post = models.ForeignKey(
        PlantInFocusPost,
        on_delete=models.CASCADE,
        default=None,
        verbose_name="Plant in Focus Posts",
        help_text="The post about the plant that this comment is related to.",
        related_name="comments",  # Allows retrieval of all comments for a post.
    )

    replying_comment = models.ForeignKey(
        "self",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="replies",
        verbose_name="Main Comment",
        help_text="The main comment to which this comment is a reply.",
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Created At",
        help_text="The timestamp indicating when the comment was created.",
    )

    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name="Updated At",
        help_text="The timestamp for the last update of the comment.",
    )

    content = models.TextField(
        verbose_name="Content",
        help_text="The text content of the comment.",
    )

    class Meta:
        """
        Meta class for specifying model options.
        Ensures that the newest comments are shown first.
        """

        ordering = ["-created_at"]
        verbose_name = "Comment"
        verbose_name_plural = "Comments"

    def __str__(self):
        """
        Returns the comment's content as a string for better readability
        in the admin panel.
        """
        return str(self.content)

    def save(self, *args, **kwargs):
        """
        Custom save method with an added check to ensure replies can only go
        two levels deep. Restricting the replies to this depth avoids the
        nesting of comments becoming overly complex which would be harder to
        display.
        """
        if self.replying_comment:
            if self.replying_comment.replying_comment:
                raise ValueError("You can't reply to a reply")

        super().save(*args, **kwargs)
