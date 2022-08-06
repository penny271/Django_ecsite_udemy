from turtle import textinput
from django import forms

class UserInfo(forms.Form):
    name = forms.CharField(label='名前', min_length=5,max_length=10)
    name = forms.CharField(max_length=50,widget=forms.TextInput(attrs={'class':'name_class','placeholder':'sample_name'}))
    age = forms.IntegerField(label='年齢')
    mail = forms.EmailField(
        label='メールアドレス',
        widget=forms.TextInput(attrs={'class':'mail-class','placeholder': 'sample@mail.com'}),
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

    def __init__(self, *args, **kwargs):
        super(UserInfo, self).__init__(*args,*kwargs)
        self.fields['job'].widget.attrs['id'] = 'id_job'
        self.fields['hobby'].widget.attrs['class'] ='hobbies_class'






def __init__(self, *args, **kwargs):
    super(UserInfo, self).__init__(*args,*kwargs)
    self.fields['job'].widgets.attrs['id']='job_id'
    self.fields['hobby'].widgets.attrs['class']='hobby_class'
