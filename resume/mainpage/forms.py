from django.forms import ModelForm, TextInput, Textarea
from .models import Revo


class RevoForm(ModelForm):
    class Meta:
        model = Revo
        fields = ["ball", "write"]
        widgets = {
            "ball": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Add your name'
                 }),
            "write": Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'What you think about this site'
                 }),
                 }