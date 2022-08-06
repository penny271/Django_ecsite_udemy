from django import forms

from .models import CartItems

class CartUpdateForm(forms.ModelForm):
    quantity = forms.IntegerField(label='数量', min_value=1)
    id = forms.CharField(widget=forms.HiddenInput())

    class Meta:
        model = CartItems
        fields = ['quantity', 'id']

    def clean(self):
        cleaned_data = super().clean()
        quantity = cleaned_data.get()
