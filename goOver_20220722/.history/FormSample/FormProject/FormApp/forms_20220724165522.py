from django import forms




class UserInfo(forms.Form):
    #- 自作のバリデーションを適用
    name = forms.CharField(label='名前', min_length=5, max_length=10)
    # name = forms.CharField(max_length=50,widget=forms.TextInput(attrs={'class':'name_class','placeholder':'sample_name'}))
    # - フィールドに対して、validators=[]で属性を追加する field ~ forms.CharField(validators = [○○]) # ○○には、djangoのライブラリ内のクラス  自作の関数を入れる
    age = forms.IntegerField(label='年齢')
    mail = forms.EmailField(
        label='メールアドレス',
        widget=forms.TextInput(attrs={'class':'mail-class','placeholder':'sample@mail.com'})
    )
    is_married = forms.BooleanField(initial=True)
    birthday = forms.DateField(initial='1990-10-10')
    salary = forms.DecimalField()
    job = forms.ChoiceField(choices=(
        (1, '正社員'),
        (2, '自営業'),
        (3, '学生'),
        (4, '無職'),
    ), widget=forms.RadioSelect
                            )
    hobby = forms.MultipleChoiceField(choices=(
        (1, 'スポーツ'),
        (2, '読書'),
        (3, '映画鑑賞'),
        (4, 'その他'),
    ), widget=forms.CheckboxSelectMultiple)
    homepage = forms.URLField(required=False)
    memo = forms.CharField(widget=forms.Textarea)


