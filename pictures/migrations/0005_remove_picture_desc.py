# Generated by Django 3.0.10 on 2020-11-12 12:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pictures', '0004_picture_created_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='picture',
            name='desc',
        ),
    ]
