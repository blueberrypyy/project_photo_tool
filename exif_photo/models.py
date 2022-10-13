from django.db import models
from exiffield.fields import ExifField

class ImageField(ExifField):
    image = models.ImageField()
    exif = ExifField(
            source='image',
            )

class DotMethodModel(models.Model):
    name = models.CharField(max_length=50)


