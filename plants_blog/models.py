"""
This module defines the PlantInFocusPost model, which represents a monthly
featured plant along with details about its, common name, environment,
culinary uses, medicinal uses, history and folklore, and images to help
identify it. The model also has fields for plants that may be mistaken for
the plant in focus. These fields are optional because there may not always be
a plant that is
confusable.  The fields for the confusable plant are fewer as it only needs
sufficient description to differentiate it from the plant that is in focus and
discount it from what is wanted.
Authors of the articles are site admins.  But in the unlikely event of an
admin deleting their account or losing their account privileges, the posts are
protected.
"""

from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError


class PlantInFocusPost(models.Model):
    """
    Represents a monthly featured plant of interest with details on its
    appearance, environment, culinary and medicinal uses, folklore, and
    historical significance. Includes information on any similar-looking plant
    that could be mistaken for the main plant, providing images and basic
    details, along with necessary warnings.
    """

    # Month choices in admin panel dropdown, when creating a plant in focus
    # post for the blog
    MONTH_CHOICES = [
        (1, "January"),
        (2, "February"),
        (3, "March"),
        (4, "April"),
        (5, "May"),
        (6, "June"),
        (7, "July"),
        (8, "August"),
        (9, "September"),
        (10, "October"),
        (11, "November"),
        (12, "December"),
    ]

    # Although admins create posts, it's conceivable that admins can change
    # So, PROTECT is used to ensure a post is kept if this should happen
    owner = models.ForeignKey(
        User,
        on_delete=models.PROTECT,
        null=True,
        blank=True,
        verbose_name="Owner",
        help_text="The user/admin that created the article.",
    )

    # Timestamp for when the post was first created.
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Creation Date and Time",
        help_text="Automatically sets date & time when the record is created",
    )
    # Timestamp for when a post is updated/changed
    updated_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Updated date & time.",
        help_text="Automatically adds date  time of update.",
    )

    # Details for main post.
    main_plant_name = models.CharField(
        max_length=255,
        verbose_name="Main Plant Name",
        help_text="Enter the common name of the main plant.",
        default="",
    )

    # Information for main plant in post
    main_plant_month = models.IntegerField(
        choices=MONTH_CHOICES,
        verbose_name="Main Plant Month",
        help_text="Select month when the main plant is likely to be found.",
        default=1,
    )
    main_plant_environment = models.TextField(
        verbose_name="Main Plant Environment",
        help_text="Describe the environment where the main plant is likely "
        "to be found.",
        default="",
    )
    culinary_uses = models.TextField(
        verbose_name="Culinary Uses",
        help_text="Describe the culinary uses of the main plant.",
        default="",
    )
    medicinal_uses = models.TextField(
        verbose_name="Medicinal Uses",
        help_text="Describe the medicinal uses of the main plant.",
        default="",
    )

    history_and_folklore = models.TextField(
        verbose_name="History and Folklore",
        help_text="Provide any historical and folklore information about the"
        "main plant.",
        default="",
    )

    main_plant_parts_used = models.TextField(
        verbose_name="Usable plant parts",
        help_text="Specify parts of the plant that are of use",
        default="Unknown",
    )

    def clean(self):
        """
        Custom validation to ensure that the default value of "Unknown" isn't
        left in the "main_plant_parts_used" field.
        If the default value it left, then a ValidationError is raised which
        prompts the admin to replace the default value with something more
        meaningful.
        """
        if self.main_plant_parts_used == "Unknown":
            raise ValidationError(
                "You must specify the plant parts used, 'Unknown' is not"
                "allowed."
            )

    main_plant_warnings = models.TextField(
        verbose_name="Plant warnings",
        help_text="Mention any warnings related to the plant that users"
        "should be aware of.",
        null=True,
        blank=True,
    )

    main_plant_image = models.ImageField(
        upload_to="images/",
        default=(
            "https://res.cloudinary.com/cheymd/image/upload/v1731062989/media/images/default_avatar_pfb93f.jpg"
        ),
        verbose_name="Main Plant Image",
        help_text="Upload an image of the main plant.",
        # Specified character length limit to prevent automatic truncation
        # issues that caused deployment failure.
        max_length=255,
    )

    # Details of plants that may be mistaken for the main_plant of interest.
    # Optional to be filled in as it maynot always be applicable.
    confusable_plant_name = models.CharField(
        max_length=255,
        verbose_name="Confusable Plant Name",
        help_text="Enter the common name of the plant that can be confused "
        "with the main plant.",
        null=True,
        blank=True,
    )
    confusable_plant_information = models.TextField(
        verbose_name="Confusable Plant Environment",
        help_text="Describe distinguishing features",
        null=True,
        blank=True,
    )
    confusable_plant_warnings = models.TextField(
        verbose_name="warnings",
        help_text="Describe any dangers of mistaking this plant for the "
        "main_plant of interest",
        null=True,
        blank=True,
    )
    confusable_plant_image = models.ImageField(
        # Folder path for storing uploaded plant images in Cloudinary
        upload_to="images/",
        default=(
            "https://res.cloudinary.com/cheymd/image/upload/v1731062989/media/images/default_avatar_pfb93f.jpg"
        ),
        verbose_name="Confusable Plant Image",
        help_text="Upload an image of the confusable plant, if needed",
        null=True,
        blank=True,
        # Specified character length limit to prevent automatic truncation
        # issues that caused deployment failure.
        max_length=500,
    )

    # String representation, returning the name of the main plant.
    def __str__(self):
        return self.main_plant_name
