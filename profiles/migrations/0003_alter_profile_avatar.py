# Generated by Django 3.2.4 on 2024-11-11 04:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0002_alter_profile_avatar'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='avatar',
            field=models.ImageField(default='images/default_avatar_pfb93f', help_text='Profile image of the user. Defaults to generic image if one is not provided', upload_to='images/', verbose_name='Profile Image'),
        ),
    ]
