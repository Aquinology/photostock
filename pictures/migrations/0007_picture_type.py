# Generated by Django 3.0.10 on 2020-11-12 14:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pictures', '0006_typepicture'),
    ]

    operations = [
        migrations.AddField(
            model_name='picture',
            name='type',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='pictures.TypePicture'),
        ),
    ]
