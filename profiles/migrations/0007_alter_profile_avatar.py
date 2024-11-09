# Generated by Django 3.2.4 on 2024-11-09 02:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0006_alter_profile_avatar'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='avatar',
            field=models.ImageField(default='https://res.cloudinary.com/cheymd/image/upload/v1731062989/media/images/default_avatar_pfb93f.jpg', help_text='Profile image of the user. Defaults to generic image if one is not provided', upload_to='images/', verbose_name='Profile Image'),
        ),
    ]
