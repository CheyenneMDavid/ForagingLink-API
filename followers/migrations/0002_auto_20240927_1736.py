# Generated by Django 3.2.4 on 2024-09-27 17:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('followers', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='follower',
            options={},
        ),
        migrations.AlterUniqueTogether(
            name='follower',
            unique_together=set(),
        ),
    ]
