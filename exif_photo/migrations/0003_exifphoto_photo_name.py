# Generated by Django 3.1.14 on 2022-12-07 21:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exif_photo', '0002_exifphoto'),
    ]

    operations = [
        migrations.AddField(
            model_name='exifphoto',
            name='photo_name',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
