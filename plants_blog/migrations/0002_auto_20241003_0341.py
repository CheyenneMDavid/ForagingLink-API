# Generated by Django 3.2.4 on 2024-10-03 03:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plants_blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='plantinfocuspost',
            name='main_plant_parts_used',
            field=models.TextField(default='Unknown', help_text='Specify parts of the plant that are of use', verbose_name='Usable plant parts'),
        ),
        migrations.AddField(
            model_name='plantinfocuspost',
            name='main_plant_warnings',
            field=models.TextField(blank=True, help_text='Mention any warnings related to the plant that users should be aware of.', null=True, verbose_name='Plant warnings'),
        ),
        migrations.AlterField(
            model_name='plantinfocuspost',
            name='confusable_plant_warnings',
            field=models.TextField(blank=True, help_text='Describe any dangers of mistaking this plant for the main_plant of interest', null=True, verbose_name='warnings'),
        ),
        migrations.AlterField(
            model_name='plantinfocuspost',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, help_text='Automatically sets date & time when the record is created', verbose_name='Creation Date and Time'),
        ),
    ]
