# Generated by Django 3.0.10 on 2020-10-30 12:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pictures', '0002_picture_author'),
    ]

    operations = [
        migrations.RenameField(
            model_name='picture',
            old_name='author',
            new_name='user',
        ),
    ]
