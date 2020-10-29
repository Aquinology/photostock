# Generated by Django 3.0.10 on 2020-10-29 15:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Picture',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=125)),
                ('picture', models.ImageField(null=True, upload_to='images/')),
                ('desc', models.TextField()),
            ],
        ),
    ]
