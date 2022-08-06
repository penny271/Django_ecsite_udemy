from django import forms

class UserInfo(forms.Form):
    name = forms.CharField(label='名前')
    age = forms.IntegerField(label='年齢')
    mail = forms.EmailField(
        label='メールアドレス',
        widget=forms.TextInput(attrs=)
    )
    is_married = forms.BooleanField(initial=True)
    birthday = forms.DateField(initial='1990-01-01')
    salary = forms.DecimalField()
    job = forms.ChoiceField(choices =(
        (1,'正社員'),
        (2,'自営業'),
        (3,'学生'),
        (4,'無職'),
    ), widget=forms.RadioSelect)
    hobby = forms.MultipleChoiceField(choices=(
        (1,'スポーツ'),
        (2,'読書'),
        (3,'映画鑑賞'),
        (4,'その他'),
    ), widget=forms.CheckboxSelectMultiple)
    homepage = forms.URLField(required=False)
    memo = forms.CharField(widget=forms.Textarea)