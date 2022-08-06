from django import forms
from django.shortcuts import get_object_or_404
from django.core.exceptions import ValidationError

from .models import CartItems

class CartUpdateForm(forms.ModelForm):
    quantity = forms.IntegerField(label='数量', min_value=1)
    id = forms.CharField(widget=forms.HiddenInput())

    class Meta:
        model = CartItems
        fields = ['quantity', 'id']

    def clean(self):
        cleaned_data = super().clean()
        quantity = cleaned_data['quantity']
        id = cleaned_data['id']
        cart_item = get_object_or_404(,pk=id)



















    def clean(self):
        cleaned_data = super().clean()
        quantity = cleaned_data.get('quantity')
        id = cleaned_data.get('id')
        cart_item = get_object_or_404(CartItems, pk=id)
        if quantity > cart_item.product.stock:
            raise ValidationError(f'在庫数を超えています。{cart_item.product}以下にしてください')
