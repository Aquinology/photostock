# Generated by Django 3.0.10 on 2020-11-12 14:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pictures', '0005_remove_picture_desc'),
    ]

    operations = [
        migrations.CreateModel(
            name='TypePicture',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
    ]