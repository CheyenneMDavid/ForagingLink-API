from django.contrib import admin
from .models import Course


class CourseAdmin(admin.ModelAdmin):
    """
    Custom admin class for the Course model.
    Configures the display of Course fields in the admin panel
    """

    # Fields to display in the list view of courses in the admin panel
    list_display = (
        "title",
        "date",
        "max_capacity",
        "available_spaces_display",
    )

    # Display the available spaces in the admin panel as a read-only field.
    readonly_fields = ("available_spaces",)

    def available_spaces_display(self, obj):
        """
        Retrieves the dynamically calculated available spaces for a course.
        Named 'available_spaces_display' instead of 'available_spaces' to
        avoid any conflicts with the 'available_spaces' property on the Course
        model, ensuring that Django admin correctly distinguishes between the
        model property and "this" method.
        """
        # Returns the number of available spaces or the message if fully
        # booked
        return obj.available_spaces

    # Sets a more readable label for the 'available_spaces_display' column in
    # the admin list view. The '.short_description' attribute displays
    # "Available Spaces" instead of the method name
    # "available_spaces_display", which was chosen to avoid conflict with the
    # existing model property.
    available_spaces_display.short_description = "Available Spaces"


# Registers the Course model with the CourseAdmin class for custom c
# onfiguration
admin.site.register(Course, CourseAdmin)
