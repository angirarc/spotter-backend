# Generated by Django 5.1.7 on 2025-03-27 15:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0008_alter_dailylog_driving_time_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='trip',
            name='dropoff_name',
            field=models.CharField(default='Default', max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='trip',
            name='pickup_name',
            field=models.CharField(default='Default', max_length=255),
            preserve_default=False,
        ),
    ]
