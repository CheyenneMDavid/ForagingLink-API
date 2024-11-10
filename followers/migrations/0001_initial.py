# Generated by Django 3.2.4 on 2024-11-10 19:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Follower',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, help_text='Date and time when the follow relationship was created.', verbose_name='Created At')),
                ('followed', models.ForeignKey(help_text='The user who is being followed.', on_delete=django.db.models.deletion.CASCADE, related_name='followed', to=settings.AUTH_USER_MODEL, verbose_name='Followed')),
                ('owner', models.ForeignKey(help_text='The user who is following another user.', on_delete=django.db.models.deletion.CASCADE, related_name='following', to=settings.AUTH_USER_MODEL, verbose_name='Owner')),
            ],
        ),
    ]
