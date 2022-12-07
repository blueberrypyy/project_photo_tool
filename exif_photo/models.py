from django.db import models
from exiffield.fields import ExifField

class ExifPhoto(models.Model):
    image = models.ImageField(upload_to='images/', null=True, blank=True)
    photo_name = models.CharField(blank=True, null=True, max_length=50)

'''
class ImageField(ExifField):
    image = models.ImageField(null=True, blank=True)
    exif = ExifField(
            source='image',
            )
'''

class DotMethodModel(models.Model):
    name = models.CharField(max_length=50)


