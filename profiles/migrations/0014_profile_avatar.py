# Generated by Django 3.2.4 on 2024-11-09 06:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0013_remove_profile_avatar'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='avatar',
            field=models.ImageField(default='https://res.cloudinary.com/cheymd/image/upload/v1731062989/media/images/default_avatar_pfb93f.jpg', help_text='Profile image of the user. Defaults to generic image if one is not provided', upload_to='images/', verbose_name='Profile Image'),
        ),
    ]
