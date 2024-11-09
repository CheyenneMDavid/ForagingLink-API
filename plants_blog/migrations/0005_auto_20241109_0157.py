# Generated by Django 3.2.4 on 2024-11-09 01:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plants_blog', '0004_auto_20241027_0530'),
    ]

    operations = [
        migrations.AlterField(
            model_name='plantinfocuspost',
            name='confusable_plant_image',
            field=models.ImageField(blank=True, default='../default_plant_image_rvlqpb.jpg', help_text='Upload an image of the confusable plant, if needed', null=True, upload_to='images/', verbose_name='Confusable Plant Image'),
        ),
        migrations.AlterField(
            model_name='plantinfocuspost',
            name='main_plant_image',
            field=models.ImageField(default='../default_plant_image_rvlqpb.jpg', help_text='Upload an image of the main plant.', upload_to='images/', verbose_name='Main Plant Image'),
        ),
    ]
