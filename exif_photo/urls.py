from django.urls import path
from .views import HomePageView, ExifPageView, DotMethodPageView

urlpatterns = [
        path('', HomePageView.as_view(), name='home'),
        path('exif/', ExifPageView.as_view(), name='exif'),
        path('dotmethod/', DotMethodPageView, name='dotmethod'),
        ]
