# Generated by Django 3.2.4 on 2024-11-11 01:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plants_blog', '0002_auto_20241111_0105'),
    ]

    operations = [
        migrations.AddField(
            model_name='plantinfocuspost',
            name='confusable_plant_image',
            field=models.ImageField(blank=True, default='images/default_plant_image_rvlqpb', help_text='Upload an image of the confusable plant, if needed', null=True, upload_to='images/', verbose_name='Confusable Plant Image'),
        ),
        migrations.AddField(
            model_name='plantinfocuspost',
            name='confusable_plant_name',
            field=models.CharField(blank=True, help_text='Enter the common name of the plant that can be confused with the main plant.', max_length=255, null=True, verbose_name='Confusable Plant Name'),
        ),
    ]
