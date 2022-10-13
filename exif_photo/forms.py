from django.forms import ModelForm, TextInput
from .models import DotMethodModel

class DotMethodForm(ModelForm):
    model = DotMethodModel
    fields = ['email']
    widgets = {
            'email': TextInput(attrs={'class': 'input', 'placeholder': 'Enter your email',}),
            }
