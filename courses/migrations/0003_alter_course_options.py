# Generated by Django 3.2.4 on 2024-09-27 17:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0002_alter_course_max_capacity'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='course',
            options={'ordering': ['-date'], 'verbose_name': 'Course', 'verbose_name_plural': 'Courses'},
        ),
    ]
