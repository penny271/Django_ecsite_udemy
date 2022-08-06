from turtle import textinput
from xml.dom import ValidationErr
from django import forms
from django.core import validators

from .models import Post

#- 自作のバリデーション


def check_name(value):
    if value == 'あああああ':
        raise validators.ValidationError('その名前は登録できません。')


class UserInfo(forms.Form):
    #- 自作のバリデーションを適用
    name = forms.CharField(label='名前', min_length=5, max_length=10, validators=[check_name])
    # name = forms.CharField(max_length=50,widget=forms.TextInput(attrs={'class':'name_class','placeholder':'sample_name'}))
    # - フィールドに対して、validators=[]で属性を追加する field ~ forms.CharField(validators = [○○]) # ○○には、djangoのライブラリ内のクラス  自作の関数を入れる
    age = forms.IntegerField(label='年齢', validators=[validators.MinValueValidator(20, message='20以上にしましょう')])
    mail = forms.EmailField(
        label='メールアドレス',
        widget=forms.TextInput(attrs={'class': 'mail-class', 'placeholder': 'sample@mail.com'}),
    )
    verify_mail = forms.EmailField(
        label='メールアドレス再入力',
        widget=forms.TextInput(attrs={'class': 'mail-class', 'placeholder': 'sample@mail.com'}),
    )
    is_married = forms.BooleanField(initial=True)
    birthday = forms.DateField(initial='1990-01-01')
    salary = forms.DecimalField()
    job = forms.ChoiceField(choices=(
        (1, '正社員'),
        (2, '自営業'),
        (3, '学生'),
        (4, '無職'),
    ), widget=forms.RadioSelect)
    hobby = forms.MultipleChoiceField(choices=(
        (1, 'スポーツ'),
        (2, '読書'),
        (3, '映画鑑賞'),
        (4, 'その他'),
    ), widget=forms.CheckboxSelectMultiple)
    homepage = forms.URLField(required=False)
    memo = forms.CharField(widget=forms.Textarea)

    def __init__(self, *args, **kwargs):
        super(UserInfo, self).__init__(*args, *kwargs)
        self.fields['job'].widget.attrs['id'] = 'id_job'
        self.fields['hobby'].widget.attrs['class'] = 'hobbies_class'

    # - 1.フィールドごとのバリデーション用のメソッドを定義する バリデーションのメソッドは、clean_フィールド名という名前で作成すると自動で実行される def clean_フィールド名(self):
    def clean_homepage(self):
        # - form.cleaned_data[‘subject’] # フォームの中の情報を扱う
        homepage = self.cleaned_data['homepage']
        if not homepage.startswith('https'):
            # * エラーの文面が画面に表示される
            raise forms.ValidationError('ホームページのURLはhttpsのみです!')

    # - 3. cleanメソッドを定義して、複数のフィールドの値をチェックする def clean(self):
    #! キー verify_mailが存在しないというエラーが発生したら、まず、
    #! ウェブ画面上のメールアドレス再入力 input にメールアドレスを入力してから
    #! 下記のコードを書くと問題なく機能する <= ウェブ上で書いていないことにより
    #! key が None でプログラムが見つけられないからエラーになると考えられる
    def clean(self):
        cleaned_data = super().clean()
        #- ユーザーから送られてきた値を取得できる
        mail = cleaned_data['mail']
        verify_mail = cleaned_data['verify_mail']
        if mail != verify_mail:
            raise forms.ValidationError('メールアドレスが一致しません!!')

#^ 共通の機能を使用するために作成
class BaseForm(forms.ModelForm):
    def save(self, *args, **kwargs):
        print(f'Form: {self.__class__.__name__}実行')
        return super(BaseForm, self).save(*args,**kwargs)

# - ModelとFormを連携させて利用したい場合に用いる。
# class PostModelForm(forms.ModelForm):
#^ 引数を変更 共通の機能を Form間で持たせたい場合に使用される
class PostModelForm(BaseForm):
    name = forms.CharField(label='名前')
    title = forms.CharField(label='タイトル')
    #- 情報を上書きできる
    memo = forms.CharField(
        label='メモ', widget=forms.Textarea(attrs={'rows': 30, 'cols': 20})
    )

    class Meta:
        model = Post
        # - fieldではなく、fields !!!
        #! NG => field = '__all__'
        fields = '__all__'
        # fields = ['name', 'title']
        # exclude = ['title']

    #* views.py の form.save()を上書きしている!!
    def save(self, *args, **kwargs):
        # commit=False で このタイミングでは save しない
        obj = super(PostModelForm, self).save(commit=False, *args, **kwargs)
        obj.name = obj.name.upper()
        print(type(obj))
        print('save実行')
        obj.save()
        return obj

    def clean_name(self):
        name = self.cleaned_data.get('name')
        if name == 'ああああ':
            raise validators.ValidationError('名前が登録できません。')
        return name

    def clean_title(self):
        title = self.cleaned_data.get('title')
        if title == 'ああああ':
            raise validators.ValidationError('そのタイトルは登録できません。')
        return title