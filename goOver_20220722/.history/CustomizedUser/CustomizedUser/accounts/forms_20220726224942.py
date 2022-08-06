from django import forms
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
# from pkg_resources import require

#- get_user_model()は現在使用しているアプリケーションのUserのモデルを返す
# 今回、ROOT_URLCONF = 'CustomizedUser.urls'を使っているのでそれが返ってくる
User = get_user_model()


class UserCreationForm(forms.ModelForm):
    password = forms.CharField(label='password', widget=forms.PasswordInput)
    confirm_password = forms.CharField(label='Password再入力', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'email', 'password')

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')
        if password != confirm_password:
            raise ValidationError('パスワードが一致しません')

    # saveメソッドをオーバーライド
    def save(self, commit=False):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data.get('password'))
        user.save()
        return user

#- 管理画面で使う
class UserChangeForm(forms.ModelForm):
    #- passwordを変更されないようにするため
    password = ReadOnlyPasswordHashField()
    website = forms.URLField(required=False) # デフォルトでTrueのところをFalseにしている
    picture = forms.FileField(required=False) # デフォルトでTrueのところをFalseにしている

    class Meta:
        model = User
        fields = ('username', 'email', 'password','is_staff', 'is_active', 'is_superuser', 'website','picture')

# バリデーション
def clean_password(self):
    # passwordが変更されないように初期値に登録されているパスワードを返す
    return self.initial['password']