from django.urls import path
from .views import HomePageView, ExifPageView, DotMethodPageView, AddressEditView, TestingPageView
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
        path('', HomePageView.as_view(), name='home'),
        path('exif/', ExifPageView, name='exif'),
        path('dotmethod/', DotMethodPageView, name='dotmethod'),
        path('address_edit/', AddressEditView, name='address_edit'),
        path('testing/', TestingPageView.as_view(), name='testing'),
        ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
