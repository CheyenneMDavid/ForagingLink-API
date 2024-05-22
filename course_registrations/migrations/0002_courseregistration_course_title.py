# Generated by Django 4.2 on 2024-05-21 15:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0001_initial'),
        ('course_registrations', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='courseregistration',
            name='course_title',
            field=models.ForeignKey(default=3, help_text='The course this registration is for.', on_delete=django.db.models.deletion.CASCADE, to='courses.course', verbose_name='Course Title'),
        ),
    ]
