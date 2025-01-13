"""
This module defines the PlantInFocusPost model, which represents a monthly
featured plant along with details about its common name, environment,
culinary uses, medicinal uses, history and folklore, and images to help
identify it. Optional fields allow for details about confusable plants.
Site admins create these posts, and they are protected if an admin's
account is deleted or privileges are removed.
"""

from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError


class PlantInFocusPost(models.Model):
    """
    Represents a monthly featured plant with details about its appearance,
    environment, uses, history, and any similar plants that may be mistaken
    for it. Includes fields for warnings and images to help differentiate.
    """

    # Dropdown menu for selecting the month when the plant is featured.
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

    # Links the post to the admin user who created it
    owner = models.ForeignKey(
        User,
        on_delete=models.PROTECT,  # Keeps posts if the admin is deleted.
        null=True,
        blank=True,
        verbose_name="Owner",
        help_text="The user/admin that created the article.",
    )

    # Automatically sets timestamps for creation and updates.
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Creation Date and Time",
        help_text="Automatically sets date & time when the record is created.",
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name="Updated Date and Time",
        help_text="Automatically sets the date and time of the last update.",
    )

    # Main plant details.
    main_plant_name = models.CharField(
        max_length=255,
        verbose_name="Main Plant Name",
        help_text="Enter the common name of the main plant.",
        default="",
    )
    main_plant_month = models.IntegerField(
        choices=MONTH_CHOICES,  # Ensures a valid month is chosen.
        verbose_name="Main Plant Month",
        help_text="Select month when the main plant is likely to be found.",
    )
    main_plant_environment = models.TextField(
        verbose_name="Main Plant Environment",
        help_text="Describe likely environment of plant",
        default="",
    )
    culinary_uses = models.TextField(
        verbose_name="Culinary Uses",
        help_text="Describe the culinary uses of the main plant.",
        default="",
    )
    medicinal_uses = models.TextField(
        verbose_name="Medicinal Uses",
        help_text="Describe the medicinal uses of main plant",
        default="",
        null=True,
        blank=True,
    )
    history_and_folklore = models.TextField(
        verbose_name="History and Folklore",
        help_text="Provide any historical and folklore information for plant.",
        default="",
    )
    main_plant_parts_used = models.TextField(
        verbose_name="Usable Plant Parts",
        help_text="Specify the parts of the plant that are useful.",
        default="",
    )
    main_plant_warnings = models.TextField(
        verbose_name="Plant Warnings",
        help_text="Potential warnings related to the plant",
        null=True,
        blank=True,
    )
    main_plant_image = models.ImageField(
        upload_to="images/",
        default="images/default_plant_image_rvlqpb",
        verbose_name="Main Plant Image",
        help_text="Upload an image of the main plant.",
    )

    # Fields for plants that may be mistaken for the main plant.
    # Optionally filled in as it may not always be applicable.
    confusable_plant_name = models.CharField(
        max_length=255,
        verbose_name="Confusable Plant Name",
        help_text="Common name of confuseable plant.",
        null=True,
        blank=True,
    )
    confusable_plant_information = models.TextField(
        verbose_name="Confusable Plant Environment",
        help_text="Describe distinguishing features of the confusable plant.",
        null=True,
        blank=True,
    )
    confusable_plant_warnings = models.TextField(
        verbose_name="Confusable Plant Warnings",
        help_text="Dangers of mistaking this plant for the main plant",
        null=True,
        blank=True,
    )
    confusable_plant_image = models.ImageField(
        upload_to="images/",
        verbose_name="Confusable Plant Image",
        help_text="Upload an image of the confusable plant, if applicable.",
        null=True,
        blank=True,
    )

    def clean(self):
        """
        Validates the model's data before saving:
        Ensures a valid month is selected for the `main_plant_month` field.
        If no `confusable_plant_name` is provided, it sets
        `confusable_plant_image` to None.
        """
        if self.main_plant_month not in dict(self.MONTH_CHOICES).keys():
            raise ValidationError(
                "You must select a valid month for the main plant!"
            )
        if not self.confusable_plant_name:
            self.confusable_plant_image = None

    def save(self, *args, **kwargs):
        """
        Runs full validation before saving the model instance.
        """
        self.full_clean()
        super().save(*args, **kwargs)

    @property
    def likes_count(self):
        """
        Returns the total number of likes for this post.
        Uses a lazy import to avoid circular imports.
        """
        from likes.models import Like

        return Like.objects.filter(plant_in_focus_post=self).count()

    @property
    def comments_count(self):
        """
        Returns the total number of comments for this post.
        Uses a lazy import to avoid circular imports.
        """
        from comments.models import Comment

        return Comment.objects.filter(plant_in_focus_post=self).count()

    def __str__(self):
        """
        Returns the name of the main plant as a string.
        """
        return self.main_plant_name
