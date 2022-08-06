from django import forms
from pkg_resources import require
#- ログイン / ユーザー情報
from .models import Users
from django.contrib.auth.password_validation import validate_password
#- Class Based View(LoginView, LogoutView)
from django.contrib.auth.forms import AuthenticationForm

class RegistForm(forms.ModelForm):
    #- model = Users にないフィールドはここで追加している!!
    #- データベースにも問題なく登録される
    username = forms.CharField(label='名前')
    age = forms.IntegerField(label='年齢', min_value=0)
    email = forms.EmailField(label='メールアドレス')
    password = forms.CharField(label='パスワード',widget=forms.PasswordInput())

    class Meta:
        model = Users
        fields = ['username','age','email','password']

    #- password暗号化
    def save(self, commit=False):
        user = super().save(commit=False)
        validate_password(self.cleaned_data['password'],user)
        user.set_password(self.cleaned_data['password'])
        user.save()
        return user

#! .ModelFormではない class UserLoginForm(forms.ModelForm):
# class UserLoginForm(forms.Form):
#     email = forms.EmailField(label='メールアドレス')
#     password = forms.CharField(label='パスワード', widget=forms.PasswordInput())

# #- views.py のclass UserLoginView(LoginView):を使用するために
# #- 再定義している
class User

# #- views.py のclass UserLoginView(LoginView):を使用するために
# #- 再定義している
# class UserLoginForm(AuthenticationForm):
#     #- ここのusernameは、一意に識別できるフィールドを指定
#     #- models.pyで指定した USERNAME_FIELD = 'email' と同じ役割
#     username = forms.EmailField(label='メールアドレス')
#     password = forms.CharField(label='パスワード', widget=forms.PasswordInput())
#     remember = forms.BooleanField(label='ログイン状態を保持する', required=False)
