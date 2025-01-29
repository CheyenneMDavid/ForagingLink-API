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
    the posts that the comments are on.

    Using SET_NULL to ensure plant_in_focus_posts are retained when an author
    deletes their account.
    their account, setting the username to inactive user.
    If the plant_in_focus_post its self deleted, then comments also delete
    using CASCADE
    Using "main_comment" as a foreign key in order to enable commenting on
    comments.
    """

    owner = models.ForeignKey(
        User,
        # If a user deletes their account, the comment remains but isn't
        # associated with the deleted user.
        on_delete=models.SET_NULL,
        null=True,
        verbose_name="Owner",
        help_text="The user who made the comment.",
    )

    plant_in_focus_post = models.ForeignKey(
        PlantInFocusPost,
        # Ensures that the comments are also deleted when the post that
        # they're associated to is deleted.
        on_delete=models.CASCADE,
        default=None,
        verbose_name="Plant in Focus Posts",
        help_text="The post about the plant that this comment is related to.",
    )

    replying_comment = models.ForeignKey(
        # Using 'self' as a foreign key, allowing the comments to reference
        # one another which enables nested replies
        "self",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="replies",
        verbose_name="Main Comment",
        help_text="The main comment to which this comment is a reply.",
    )

    created_at = models.DateTimeField(
        # Sets the comment creation time to 'now'
        auto_now_add=True,
        verbose_name="Created At",
        help_text="The timestamp indicating when the comment was created.",
    )

    updated_at = models.DateTimeField(
        # Sets the comment update time to 'now'
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

        # Orders comments by creation time, with newest first
        ordering = ["-created_at"]
        verbose_name = "Comment"
        verbose_name_plural = "Comments"

    def __str__(self):
        """
        Returning the comment as a string so that the comment can be read in
        the admin panel, making it easier to moderate.
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
            print("Replying to the comment ID:", self.replying_comment.id)

            if self.replying_comment.replying_comment:
                print("Additional nested reply detected! Raising error.")
                raise ValueError(
                    "You can't reply to a reply beyond two levels."
                )

        # Call the superclass's save method to handle saving after applying
        # the custom logic that limits comments to only 2 levels deep.
        super().save(*args, **kwargs)
