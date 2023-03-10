# Generated by Django 4.1 on 2022-12-23 12:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_event_is_published'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='Event_type',
            field=models.CharField(choices=[('Birthday', 'Birthday'), ('Marriage', 'Marriage'), ('Anniversary', 'Anniversary'), ('Other', 'Other')], default='1', max_length=155),
        ),
        migrations.AlterField(
            model_name='event',
            name='event_date',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='event',
            name='info_added_on',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
