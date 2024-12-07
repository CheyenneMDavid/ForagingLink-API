# Generated by Django 3.2.25 on 2024-11-27 07:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plants_blog', '0005_plantinfocuspost_main_plant_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='plantinfocuspost',
            name='confusable_plant_image',
            field=models.ImageField(blank=True, help_text='Upload an image of the confusable plant, if needed', null=True, upload_to='images/', verbose_name='Confusable Plant Image'),
        ),
        migrations.AlterField(
            model_name='plantinfocuspost',
            name='main_plant_month',
            field=models.IntegerField(choices=[(1, 'January'), (2, 'February'), (3, 'March'), (4, 'April'), (5, 'May'), (6, 'June'), (7, 'July'), (8, 'August'), (9, 'September'), (10, 'October'), (11, 'November'), (12, 'December')], help_text='Select month when the main plant is likely to be found.', verbose_name='Main Plant Month'),
        ),
        migrations.AlterField(
            model_name='plantinfocuspost',
            name='main_plant_parts_used',
            field=models.TextField(default='', help_text='Specify parts of the plant that are of use', verbose_name='Usable plant parts'),
        ),
        migrations.AlterField(
            model_name='plantinfocuspost',
            name='medicinal_uses',
            field=models.TextField(blank=True, default='', help_text='Describe the medicinal uses of the main plant.', null=True, verbose_name='Medicinal Uses'),
        ),
    ]
