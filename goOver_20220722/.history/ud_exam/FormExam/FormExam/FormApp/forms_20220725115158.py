from django import forms
from .models import Students


# class StudentInsertForm(forms.ModelForm):
#     name = forms.CharField(label='名前')
#     age = forms.IntegerField(label='年齢')
#     grade = forms.IntegerField(label='学年')
#     #- mediaフォルダもsutdent/フォルダも作る必要なし
#     #- settings.pyで保存場所を指定済みのため
#     picture = forms.FileField(label='ファイルアップロード')

#     #- model と fieldsが必須
#     class Meta:
#         model = Students