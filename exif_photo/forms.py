from django.forms import ModelForm, TextInput
from .models import DotMethodModel, ExifPhoto

class DotMethodForm(ModelForm):
    model = DotMethodModel
    fields = ('email')
    widgets = {
            'email': TextInput(attrs={'class': 'input', 'placeholder': 'Enter your email',}),
            }

class ExifPhotoForm(ModelForm):
    model = ExifPhoto
    fields = ('image')
    labels = {
            'image': '',
            }
