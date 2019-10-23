from django import forms
from .models import Cart

class TickForm(forms.ModelForm):
    tick = forms.BooleanField(label = 'ok')
    class Meta:
        model = Cart
        fields = ['product','quantity']
        widgets = {
            'product':forms.HiddenInput,
        }

        