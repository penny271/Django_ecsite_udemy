from .models import Students
from django import forms

class StudentInsertForm(forms.ModelForm):

    #- 情報の上書き、追加
    name = forms.CharField(label='名前')
    age = forms.IntegerField(label='年齢')
    grade = forms.IntegerField(label='学年')
    picture = forms.FileField(label='ファイルアップロード')

    class Meta:
        model = Students
        fields = '__all__'

#* 編集用
#- 引数をforms.ModelForm ではなく forms.Formにする
class StudentUpdateForm(forms.Form):

    #- 情報の上書き、追加
    name = forms.CharField(label='名前')
    age = forms.IntegerField(label='年齢')
    grade = forms.IntegerField(label='学年')
    picture = forms.FileField(label='ファイルアップロード',required=False)

#