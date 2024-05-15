# Configuration for Like model in Django admin panel.

from django.contrib import admin
from likes.models import Like


@admin.register(Like)
class LikeAdmin(admin.ModelAdmin):
    """
    Admin class for managing Like instances in the Django admin interface.
    """

    list_display = (
        "id",
        "owner",
        "plant_in_focus_post",
        "comment",
        "created_at",
    )
    list_filter = ("created_at", "owner")
    search_fields = (
        "owner__username",
        "plant_in_focus_post__main_plant_name",
        "comment__content",
    )
