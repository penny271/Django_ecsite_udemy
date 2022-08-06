# from .models import Students
from django import forms

# class StudentInsertForm(forms.ModelForm):

#     #- 情報の上書き、追加
#     name = forms.CharField(label='名前')
#     age = forms.IntegerField(label='年齢')
#     grade = forms.IntegerField(label='学年')
#     picture = forms.FileField(label='ファイルアップロード')

#     class Meta:
#         model = Students
#         fields = '__all__'


class StudentInsertForm(forms.ModelForm):
    name = forms.CharField(label='名前')
    age = forms.IntegerField()
    grade = forms.IntegerField()
    #- mediaフォルダもsutdent/フォルダも作る必要なし
    #- settings.pyで保存場所を指定済みのため
    picture = forms.FileField(upload_to='student')

    import 

    class Meta:
        model = Student
        db_table= 'students'

#* 編集用
#- 引数をforms.ModelForm ではなく forms.Formにする
class StudentUpdateForm(forms.Form):

    #- 情報の上書き、追加
    name = forms.CharField(label='名前')
    age = forms.IntegerField(label='年齢')
    grade = forms.IntegerField(label='学年')
    picture = forms.FileField(label='ファイルアップロード',required=False)

#* 削除用
#- 削除するには、pkであるidさえわかればよい
class StudentDeleteForm(forms.Form):
    #- widget=forms.HiddenInput 画面に表示させない設定
    id = forms.IntegerField(widget=forms.HiddenInput)
    # id = forms.IntegerField() <= #! これだとidが表示されてかっこ悪い