# Generated by Django 3.2.4 on 2024-09-27 17:36

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('courses', '0003_alter_course_options'),
        ('course_registrations', '0002_courseregistration_course_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='courseregistration',
            name='course_title',
            field=models.ForeignKey(default=3, help_text='Enter the title of the course for this registration.', on_delete=django.db.models.deletion.CASCADE, to='courses.course', verbose_name='Course Title'),
        ),
        migrations.AlterField(
            model_name='courseregistration',
            name='owner',
            field=models.ForeignKey(help_text='Select the user this registration belongs to.', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Owner'),
        ),
    ]
