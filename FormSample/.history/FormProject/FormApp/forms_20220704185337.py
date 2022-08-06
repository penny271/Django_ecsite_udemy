from turtle import textinput
from django import forms
from django.core import validators

def check_name(value):
    if value == 'あああああ':
        raise validators.ValidationError('その名前は登録できません。')

class UserInfo(forms.Form):
    name = forms.CharField(label='名前', min_length=5,max_length=10, validators=[check])
    name = forms.CharField(max_length=50,widget=forms.TextInput(attrs={'class':'name_class','placeholder':'sample_name'}))
    #-2. フィールドに対して、validators=[]で属性を追加する field ~ forms.CharField(validators = [○○]) # ○○には、djangoのライブラリ内のクラス  自作の関数を入れる
    age = forms.IntegerField(label='年齢', validators=[validators.MinValueValidator(20, message='20以上にしましょう')])
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

    #- 1.フィールドごとのバリデーション用のメソッドを定義する バリデーションのメソッドは、clean_フィールド名という名前で作成すると自動で実行される def clean_フィールド名(self):
    def clean_homepage(self):
        #- form.cleaned_data[‘subject’] # フォームの中の情報を扱う
        homepage = self.cleaned_data['homepage']
        if not homepage.startswith('https'):
            #* エラーの文面が画面に表示される
            raise forms.ValidationError('ホームページのURLはhttpsのみです!')




    # def __init__(self, *args, **kwargs):
    #     super(UserInfo, self).__init__(*args,*kwargs)
    #     self.fields['job'].widgets.attrs['id']='job_id'
    #     self.fields['hobby'].widgets.attrs['class']='hobby_class'
