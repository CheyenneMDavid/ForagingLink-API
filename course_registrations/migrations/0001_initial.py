# Generated by Django 4.2 on 2024-05-21 00:35

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
            name='CourseRegistration',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(help_text='The email address of the user.', max_length=255, verbose_name='Email')),
                ('phone', models.CharField(help_text='The phone number of the user.', max_length=20, verbose_name='Phone')),
                ('registration_date', models.DateTimeField(auto_now=True, help_text='The date and time of registration.', verbose_name='Registration Date')),
                ('status', models.CharField(choices=[('Pending', 'Pending'), ('Confirmed', 'Confirmed'), ('Cancelled', 'Cancelled')], default='Pending', help_text='The current status of the registration.', max_length=50, verbose_name='Status')),
                ('dietary_restrictions', models.TextField(blank=True, help_text='Any dietary restrictions of the user.', null=True, verbose_name='Dietary Restrictions')),
                ('is_driver', models.BooleanField(default=False, help_text='Indicates if the user is a driver.', verbose_name='Is Driver')),
                ('ice_name', models.CharField(help_text='Name of the emergency contact person.', max_length=255, verbose_name='Emergency Contact Name')),
                ('ice_number', models.CharField(help_text='Phone number for the emergency contact, person.', max_length=20, verbose_name='Emergency Contact Number')),
                ('owner', models.ForeignKey(help_text='The user this registration belongs to.', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Owner')),
            ],
        ),
    ]
