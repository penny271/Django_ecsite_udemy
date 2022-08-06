from importlib.metadata import files
from django import forms
from django.contrib.auth.models import User
#- Profileクラスをimport user.models というpathをたどっている
from user.models import Profile

class UserForm(forms.ModelForm):
    username = forms.CharField(label='名前')
    email = forms.CharField(label='メールアドレス')
    #- widget=forms.PasswordInput() passwordを見えなくする
    password = forms.CharField(label='パスワード', widget=forms.PasswordInput())
    class Meta():
        model = User
        fields = ('username', 'email', 'password')

class ProfileForm(forms.ModelForm):
    website = forms.URLField(label='ホームページ')
    picture = forms.FileField(label='写真')

    class Meta():
        model = Profile
        fields = ('website', 'picture')

class LoginForm():
    username = forms.CharField(label='名前', max_length=150)
    password = forms.CharField(label='名前', widget=forms.PasswordInput())
    confirm_password = forms.CharField(label='パスワード再入力', widget=forms.PasswordInput())

    def clean(self):
        cleaned_data