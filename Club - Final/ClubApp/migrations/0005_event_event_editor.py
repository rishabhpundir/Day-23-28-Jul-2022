# Generated by Django 3.2.4 on 2022-07-28 04:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ClubApp', '0004_alter_event_venue_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='event_editor',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
