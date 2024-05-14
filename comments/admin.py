"""
Admin configuration to register the model with the Django admin interface,
allowing administrators to search the comments according to content, who wrote
the comment, which particular plant they commented on, and filter according to
who wrote it, when it was written and when it was updated.

"""

from django.contrib import admin
from .models import Comment


class CommentAdmin(admin.ModelAdmin):
    """
    Administration object for the Comment model.
    """

    list_display = (
        "content",
        "owner",
        "created_at",
        "updated_at",
    )

    search_fields = [
        "content",
        "owner__username",
        "plant_in_focus_post__main_plant_name",
    ]

    list_filter = ("owner", "created_at", "updated_at")


admin.site.register(Comment, CommentAdmin)
