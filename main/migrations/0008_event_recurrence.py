# Generated by Django 5.0.3 on 2024-04-09 07:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_alter_event_event_type_alter_event_location'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='recurrence',
            field=models.CharField(blank=True, choices=[('daily', 'Daily'), ('weekly', 'Weekly'), ('monthly', 'Monthly'), ('yearly', 'Yearly')], max_length=10, null=True),
        ),
    ]