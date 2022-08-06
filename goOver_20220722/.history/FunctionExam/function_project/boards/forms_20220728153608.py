from django import forms
from .models import Themes, Comments

class CreateThemeForm(forms.ModelForm):
    title = forms.CharField(label='タイトル')

    class Meta:
        model = Themes
        fields = ('title',)

class DeleteThemeForm(forms.ModelForm):

    class Meta:
        model = Themes
        #!- fieldsは空で問題なし 削除するためのclassなので
        fields = []

class PostCom mment', )