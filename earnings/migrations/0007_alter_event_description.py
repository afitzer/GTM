# Generated by Django 4.2 on 2023-05-22 02:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('earnings', '0006_alter_trip_flights_alter_trip_hotels'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='description',
            field=models.CharField(max_length=200),
        ),
    ]
