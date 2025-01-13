"""
This module defines the Comment model, enabling users to comment on posts
and reply to other comments. Replies are limited to two levels of depth
to prevent overly complex nesting.
"""

from django.db import models
from django.contrib.auth.models import User


class Comment(models.Model):
    """
    Represents a user-generated comment associated with a specific post.
    Supports replying to comments with a restriction to two levels of depth.
    """

    owner = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,  # Keeps comments if account is deleted
        null=True,
        verbose_name="Owner",
        help_text="The user who made the comment.",
    )

    plant_in_focus_post = models.ForeignKey(
        "plants_blog.PlantInFocusPost",
        on_delete=models.CASCADE,  # Deletes comments if post is deleted
        verbose_name="Plant in Focus Post",
        help_text="The post about the plant that this comment is related to.",
    )

    replying_comment = models.ForeignKey(
        "self",
        on_delete=models.CASCADE,  # Deletes replies if comment is deleted
        null=True,
        blank=True,
        related_name="replies",  # Enables reverse lookup for replies
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

    @property
    def replies_count(self):
        """
        Calculates the number of replies for this comment.
        """
        from comments.models import (
            Comment,
        )  # Lazy import to avoid circular imports

        return Comment.objects.filter(replying_comment=self).count()

    class Meta:
        """
        Specifies model options, such as default ordering by creation date.
        """

        ordering = ["-created_at"]  # Newest comments appear first
        verbose_name = "Comment"
        verbose_name_plural = "Comments"

    def __str__(self):
        """
        Returns the comment content for better readability in the admin panel.
        """
        return str(self.content)

    def save(self, *args, **kwargs):
        """
        Overrides save to ensure replies do not exceed two levels of nesting.
        """
        if self.replying_comment and self.replying_comment.replying_comment:
            raise ValueError("You cannot reply to a reply beyond two levels.")
        super().save(*args, **kwargs)
