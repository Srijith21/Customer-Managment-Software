# Generated by Django 4.1 on 2022-12-22 19:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_alter_event_event_time_type_alter_event_event_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='is_published',
            field=models.BooleanField(default=True),
        ),
    ]