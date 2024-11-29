# Generated by Django 3.2.25 on 2024-11-29 17:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plants_blog', '0010_auto_20241129_1716'),
    ]

    operations = [
        migrations.AddField(
            model_name='plantinfocuspost',
            name='confusable_plant_image',
            field=models.ImageField(blank=True, help_text='Upload an image of the confusable plant, if needed', null=True, upload_to='images/', verbose_name='Confusable Plant Image'),
        ),
        migrations.AddField(
            model_name='plantinfocuspost',
            name='confusable_plant_information',
            field=models.TextField(blank=True, help_text='Describe distinguishing features', null=True, verbose_name='Confusable Plant Environment'),
        ),
        migrations.AddField(
            model_name='plantinfocuspost',
            name='confusable_plant_name',
            field=models.CharField(blank=True, help_text='Enter the common name of the plant that can be confused with the main plant.', max_length=255, null=True, verbose_name='Confusable Plant Name'),
        ),
        migrations.AddField(
            model_name='plantinfocuspost',
            name='confusable_plant_warnings',
            field=models.TextField(blank=True, help_text='Describe any dangers of mistaking this plant for the main_plant of interest', null=True, verbose_name='warnings'),
        ),
    ]
