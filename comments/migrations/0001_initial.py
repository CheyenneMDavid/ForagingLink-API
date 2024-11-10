# Generated by Django 3.2.4 on 2024-11-10 16:51

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('plants_blog', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, help_text='The timestamp indicating when the comment was created.', verbose_name='Created At')),
                ('updated_at', models.DateTimeField(auto_now=True, help_text='The timestamp for the last update of the comment.', verbose_name='Updated At')),
                ('content', models.TextField(help_text='The text content of the comment.', verbose_name='Content')),
                ('owner', models.ForeignKey(help_text='The user who made the comment.', null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='Owner')),
                ('plant_in_focus_post', models.ForeignKey(default=None, help_text='The post about the plant that this comment is related to.', on_delete=django.db.models.deletion.CASCADE, to='plants_blog.plantinfocuspost', verbose_name='Plant in Focus Posts')),
                ('replying_comment', models.ForeignKey(blank=True, help_text='The main comment to which this comment is a reply.', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='replies', to='comments.comment', verbose_name='Main Comment')),
            ],
            options={
                'verbose_name': 'Comment',
                'verbose_name_plural': 'Comments',
                'ordering': ['-created_at'],
            },
        ),
    ]
