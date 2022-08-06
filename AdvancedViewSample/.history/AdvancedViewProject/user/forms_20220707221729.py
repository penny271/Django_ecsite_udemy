from django import forms
from django.contrib.auth.models import User
#- Profileクラスをimport user.models というpathをたどっている
from user.models import Profile


class UserForm(forms.ModelForm):
    password = forms.CharField(label='パスワード', widget=forms.PasswordInput())
    class Meta():
        model = User