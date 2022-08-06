from django import forms




class UserInfo(forms.Form):
    #- 自作のバリデーションを適用
    name = forms.CharField(label='名前', min_length=5, max_length=10)
    # name = forms.CharField(max_length=50,widget=forms.TextInput(attrs={'class':'name_class','placeholder':'sample_name'}))
    # - フィールドに対して、validators=[]で属性を追加する field ~ forms.CharField(validators = [○○]) # ○○には、djangoのライブラリ内のクラス  自作の関数を入れる
    age = forms.IntegerField(label='年齢')
    mail = forms.EmailField(
        label='メールアドレス',
    )


if request.method == ‘POST’: # リクエストメソッドがPOSTの場合
    form = forms.UserInfo(request.POST) # リクエストを処理してFormの型に変換 if form.is_valid(): # formの中のフィールドの値が正しいかチェックする

form.cleaned_data[‘subject’] # フォームの中の情報を扱う