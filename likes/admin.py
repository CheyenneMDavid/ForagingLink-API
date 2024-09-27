# Configuration for Like model in Django admin panel.

from django.contrib import admin
from likes.models import Like


@admin.register(Like)
class LikeAdmin(admin.ModelAdmin):
    """
    Admin class for managing Like instances in the Django admin interface.
    """

    # Lists of fields that are displayed in the admin panel.
    list_display = (
        "id",
        "owner",
        "plant_in_focus_post",
        "comment",
        "created_at",
    )
    # Filters that can be applied in the admin panel.
    list_filter = ("created_at", "owner")
    # Fields that can be used to search from within the admin panel.
    search_fields = (
        "owner__username",
        "plant_in_focus_post__main_plant_name",
        "comment__content",
    )
