from django.contrib import admin
from .models import ExifPhoto, ImageField, DotMethodModel

admin.site.register(ExifPhoto)
admin.site.register(DotMethodModel)


