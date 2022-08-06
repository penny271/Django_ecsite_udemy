from django import forms
from django.shortcuts import get_object_or_404
from django.core.exceptions import ValidationError

from .models import CartItems, Addresses

class CartUpdateForm(forms.ModelForm):
    quantity = forms.IntegerField(label='数量', min_value=1)
    id = forms.CharField(widget=forms.HiddenInput())

    class Meta:
        model = CartItems
        fields = ['quantity', 'id']

    def clean(self):
        cleaned_data = super().clean()
        quantity = cleaned_data.get('quantity')
        id = cleaned_data.get('id')
        cart_item = get_object_or_404(CartItems, pk=id)
        if quantity > cart_item.product.stock:
            raise ValidationError(f'在庫数を超えています。{cart_item.product}以下にしてください')

class AddressInputForm(forms.ModelForm):
    address = forms.CharField(label='住所', widget=forms.TextInput(attrs={'size': '80'}))

    class Meta:
        model=Addresses
        fields = ['zip_code', 'prefecture', 'address']
        #- まとめてlabelを変更できる!
        labels = {
            'zip_code':'郵便場号',
            'prefecture': '都道府県',
        }

    def save(self):
        return super().save(commit)
