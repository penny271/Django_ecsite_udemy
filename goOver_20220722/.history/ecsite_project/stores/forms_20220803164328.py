from django import forms

from .models import CartItems

class CartUpdateForm(forms.ModelForm):
    quantity = forms.IntegerField(label='数量', min_value=1)
    id = forms.CharField(widget=input.)