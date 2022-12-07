from django.forms import ModelForm, TextInput
from .models import DotMethodModel, ExifPhoto

class DotMethodForm(ModelForm):
    class Meta:
        model = DotMethodModel
        fields = ('name',)
        widgets = {
                'email': TextInput(attrs={'class': 'input', 'placeholder': 'Enter your email',}),
                }

class ExifPhotoForm(ModelForm):
    class Meta:
        model = ExifPhoto
        fields = ('image', 'photo_name')
        labels = {
                'image': '',
                }
