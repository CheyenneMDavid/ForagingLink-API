# Configuration for Like model in Django admin panel.

from django.contrib import admin
from likes.models import Like


@admin.register(Like)
class LikeAdmin(admin.ModelAdmin):
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
        "plant_in_focus_post__title",
        "comment__content",
    )
