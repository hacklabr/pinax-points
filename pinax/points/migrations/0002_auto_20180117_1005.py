# Generated by Django 2.0.1 on 2018-01-17 10:05

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('pinax_points', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='awardedpointvalue',
            name='timestamp',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
