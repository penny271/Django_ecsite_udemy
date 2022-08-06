from wsgiref import validate
from django import forms
from .models import Users
from django.contrib.auth.password_validation import validate_password


class RegistForm(forms.ModelForm):
    username = forms.CharField(label='名前')
    age = forms.IntegerField(label='年齢', min_value=0)
    email = forms.EmailField(label='メールアドレス')
    password = forms.CharField(label='パスワード', widget=forms.PasswordInput())
    confirm_password = forms.CharField(label='パスワード再入力', widget=forms.PasswordInput())

    class Meta():
        model = Users
        fields = ('username', 'age', 'email', 'password')

    #- 自動で実行される
    #- パスワードの再入力を確認するためのもの
    def clean(self):
        #- def save()のようにself.cleand_data[]は使えない - インスタンス化していないため!
        cleaned_data = super().clean()
        password = cleaned_data['password']
        confirm_password = cleaned_data['confirm_password']
        if password != confirm_password:
            raise forms.ValidationError('パスワードが異なります')

    #- passwordのvalidation - settings.pyのものを適用させる
    #- password暗号化させる 2点の目的
    def save(self, commit=False):
        #- 親クラスのsave()を呼び出している
        #- ユーザが戻り値として返ってくる
        user = super().save(commit=False)
        #- passwordのvalidation - settings.pyのものを適用
        validate_password(self.cleaned_data['password'],user)
        #- passwordの暗号化
        user.set_password(self.cleaned_data['password'])
        user.save()
        #- 保存したデータを返す
        return user

class LoginForm(forms.Form):
    email = forms.CharField(label='メールアドレス')
    password = forms.CharField(label='パスワード',widget=forms.PasswordInput)

    password = forms.CharField(widget=forms.PasswordInput())

# #- ModelFormでデータ、(パスワードの更新0
# class UserEditForm(forms.ModelForm):
#     username = forms.CharField(label='名前')
#     age = forms.IntegerField(label='年齢', min_value=0)
#     email = forms.EmailField(label='メールアドレス')
#     picture = forms.FileField(label='写真', required=False)

#     class Meta:
#         model = Users
#         fields = ('username', 'age', 'email', 'picture')

# #- ModelFormでデータ、パスワードの更新
# class PasswordChangeForm(forms.ModelForm):
#     password = forms.CharField(label='パスワード', widget=forms.PasswordInput())
#     confirm_password = forms.CharField(label='パスワード再入力', widget=forms.PasswordInput())

#     class Meta():
#         model = Users
#         fields = ('password',)

#     def clean(self):
#         cleaned_data = super().clean()
#         password = cleaned_data['password']
#         confirm_password = cleaned_data['confirm_password']
#         if password != confirm_password:
#             raise forms.ValidationError('パスワードが異なります')

#     def save(self, commit=False):
#         #- 親クラスのsave()を呼び出している
#         #- ユーザが戻り値として返ってくる
#         user = super().save(commit=False)
#         #- passwordのvalidation - settings.pyのものを適用
#         validate_password(self.cleaned_data['password'],user)
#         #- passwordの暗号化
#         user.set_password(self.cleaned_data['password'])
#         user.save()
#         #- 保存したデータを返す
#         return user
