from django import forms
from .models import Books
from datetime import datetime

class BookForm(forms.ModelForm):
    # name = forms.CharField(max_length=255,label='名前')
    # description = forms.CharField(max_length=1000)
    # price = forms.IntegerField()

    class Meta:
        model = Books
        fields = ['name', 'description', 'price']

    def save(self, *args, **kwargs):
        #- Booksクラスのインスタンスがobjに入る
        #- もともとBooksクラス内のsave()から呼び出されているため
        obj = super(BookForm, self).save(commit=False)
        obj.create_at = datetime.now()
        obj.update_at = datetime.now()
        obj.save()
        return obj

class BookUpdateForm(forms.ModelForm):
    # name = forms.CharField(max_length=255,label='名前')
    # description = forms.CharField(max_length=1000)
    # price = forms.IntegerField()

    class Meta:
        model = Books
        fields = ['name', 'description', 'price']

    def save(self, *args, **kwargs):
        #- Bookクラスのインスタンスがobjに入る
        obj = super(BookUpdateForm, self).save(commit=False)
        # obj.create_at = datetime.now() 更新するだけなので不要
        obj.update_at = datetime.now()
        obj.save()
        return obj

class PictureUploadForm(forms.ModelForm):
    picture = forms.FileField(required=False)

    class Meta:
        model = Pictures
        fields = ['picture',]

    def save(self, *args, **kwargs):
        obj = super(PictureUploadForm,self).save(commit=False)
        obj.create_at = datetime.now()
        obj.update_at = datetime.now()
        #- kwargs['book']は、views.py の picture_form.save(book = book)から来ている
        obj.book = kwargs['book']
        obj.save()
        return obj



class Person:
    """人 クラス"""
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def self_introduce(self):
        print(f"私の名前は{self.name}、{self.age}才です。")


class SoccerPlayer(Person):
    """サッカー選手 クラス"""

    # 親クラスと同じ名前のメソッドを定義する。
    def self_introduce(self):
        print(f"サッカー選手をやっている{self.name}と申します。")

    def kick(self):
        print("キック!")


s1 = SoccerPlayer("本田", 20)

# 子クラスのself_introduceが実行される
s1.self_introduce()
# 出力結果
サッカー選手をやっている本田と申します。

# super(<子クラス名>, <インスタンス>)で親クラスのメソッドを実行できる
super(SoccerPlayer, s1).self_introduce()

# 出力結果(Personクラスのself_introduceが実行される)

