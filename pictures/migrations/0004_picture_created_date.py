# Generated by Django 3.0.10 on 2020-11-12 12:30

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('pictures', '0003_auto_20201030_1819'),
    ]

    operations = [
        migrations.AddField(
            model_name='picture',
            name='created_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
