from django import forms
from django.shortcuts import get_object_or_404
from django.core.exceptions import ValidationError
from django.core.cache import cache

from .models import CartItems, Addresses

class CartUpdateForm(forms.ModelForm):
    quantity = forms.IntegerField(label='数量',min_value=1)
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
            raise ValidationError(f'在庫数を超えています。{cart_item.product.stock}以下にしてください。')

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

    #- saveと同時にユーザを設定する
    def save(self):
        address = super().save(commit=False)
        #- self.user の self は AddressInputFormクラスのインスタンス
        #- views.pyの form.user = self.request.userが selfに入っており、
        #- そのself.request.user を address.userに入れている!!
        address.user = self.user
        try:
            address.validate_unique() # uniqueエラーが発生した場合、ValidationErrorを発生させる 問題なければ、その下のコードが実行される
            address.save()
        except ValidationError as e:
            address = get_object_or_404(
                Addresses, user=self.user,
                prefecture = address.prefecture,
                zip_code = address.zip_code,
                address=address.address,
            )
        cache.set(f'address_user_{self.user.id}',address)
        return address

