# Generated by Django 3.2.4 on 2024-11-10 16:51

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('season', models.CharField(choices=[('', 'Select Season'), ('Spring', 'Spring'), ('Summer', 'Summer'), ('Autumn', 'Autumn')], default='', help_text='Select the season during which the course is offered.', max_length=25, verbose_name='Season')),
                ('title', models.CharField(help_text='Enter the title of the course.', max_length=255, verbose_name='Course Title')),
                ('date', models.DateField(help_text='Enter the date on which the course is held.', verbose_name='Course Date')),
                ('description', models.TextField(help_text='Provide a detailed description of the course.', verbose_name='Course Description')),
                ('location', models.CharField(help_text='Enter the location where the course will take place.', max_length=255, verbose_name='Course Location')),
                ('max_capacity', models.PositiveIntegerField(default=10, help_text='The maximum number of participants for the course.', validators=[django.core.validators.MaxValueValidator(10)], verbose_name='Maximum Capacity')),
            ],
            options={
                'verbose_name': 'Course',
                'verbose_name_plural': 'Courses',
                'ordering': ['-date'],
            },
        ),
    ]
