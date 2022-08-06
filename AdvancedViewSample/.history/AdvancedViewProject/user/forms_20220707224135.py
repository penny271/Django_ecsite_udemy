from importlib.metadata import files
from django import forms
from django.contrib.auth.models import User
#- Profileクラスをimport user.models というpathをたどっている
from user.models import Profile

class UserForm(forms.ModelForm):
    username = forms.CharField(label='名前', widget=forms.PasswordInput())
    email = forms.CharField(label='メールアドレス', widget=forms.PasswordInput())
    password = forms.CharField(label='パスワード', widget=forms.PasswordInput())
    class Meta():
        model = User
        fields = ('username', 'email', 'password')

class ProfileForm(forms.ModelForm):
    website = forms.URLField(label='ホームページ')
    picture = forms.FileField(label='写真')

    class Meta():
        model = Profile
        fields = ('username', 'email', 'password')