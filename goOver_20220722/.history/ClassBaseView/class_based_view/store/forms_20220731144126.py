from django import forms
from .models import Books, Pictures
from datetime import datetime

class BookForm(forms.ModelForm):
    name = forms.CharField(max_length=255,label='名前')
    description = forms.CharField(max_length=1000)
    price = forms.IntegerField()

    class Meta:
        model = Books
        fields = ['name', 'description', 'price']

    def save(self, *args, **kwargs):
        print(super(BookForm, self))
        print('forms.ModelForm: ', forms.ModelForm)
        #- Booksクラスのインスタンスがobjに入る
        #- 親クラスのforms.ModelFormのsave()が呼び出され、class Metaでmodels = Booksとなっているので、Booksクラスのインスタンスを取得できる!!
        print(dir(BookForm))
        obj = super(BookForm, self).save(commit=False)
        # obj = self.save(commit=False) #! 不可 recursionError
        print('★: ', obj)
        obj.create_at = datetime.now()
        obj.update_at = datetime.now()
        obj.save()
        return obj

class BookUpdateForm(forms.ModelForm):
    name = forms.CharField(max_length=255,label='名前')
    description = forms.CharField(max_length=1000)
    price = forms.IntegerField()

    class Meta:
        model = Books
        fields = ['name', 'description', 'price']

    # def save(self, *args, **kwargs):
    #     #- Bookクラスのインスタンスがobjに入る
    #     obj = super(BookUpdateForm, self).save(commit=False)
    #     # obj.create_at = datetime.now() 更新するだけなので不要
    #     obj.update_at = datetime.now()
    #     obj.save()
    #     return obj

class PictureUploadForm(forms.ModelForm):
    picture = forms.FileField(required=False)

    class Meta:
        model = Pictures
        fields = ['picture',]

    def save(self, *args, **kwargs):
        obj = super(PictureUploadForm,self).save(commit=False)
        obj.create_at = datetime.now()
        obj.update_at = datetime.now()
        #- kwargs['book']は、views.py の picture_form.save(book = book)から来ている。外部キーを設定している
        obj.book = kwargs['book']
        obj.save()
        return obj