from django import forms

class UserInfo(forms.Form):
    name = forms.CharField(label='名前')
    age = forms.IntegerField(label='年齢')
    mail = forms.EmailField(label='名前')
    is_married = forms.BooleanField()
    birthday = forms.DateField()
    salary = forms.DecimalField()
    job = forms.ChoiceField(choices =(
        (1,'正社員'),
        (2,'自営業'),
        (3,'学生'),
        (4,'無職'),
    ))
    hobby = forms.MultipleChoiceField(choices=(
        (1,'スポーツ'),
        (2,'読書'),
        (3,'映画鑑賞'),
        (4,'その他'),

    ))
    homepage = forms.URLField()