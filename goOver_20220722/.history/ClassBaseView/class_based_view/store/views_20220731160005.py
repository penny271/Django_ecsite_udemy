from datetime import datetime
from genericpath import isfile
from django.shortcuts import get_object_or_404, render, redirect
from django.views.generic.base import (
    View, TemplateView, RedirectView
)
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic.edit import (
    CreateView, UpdateView, DeleteView,FormView,
)
from requests import delete
from . import forms
from datetime import datetime
from .models import Books, Pictures
from django.urls import reverse_lazy
#- 他のViewクラスに多重継承させることで使用できる
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages


class IndexView(View):

    def get(self, request, *args, **kwargs):
        book_form = forms.BookForm()
        return render(request, 'index.html', context={
            'book_form': book_form
        })

    # POSTだった場合はこの関数が自動的に呼び出される
    #! 記載がないと"POST /store/index/ HTTP/1.1" 405 0 エラーが出る
    #! 405 エラー (Method Not Allowed) というエラー
    def post(self, request,*args, **kwargs):
        book_form = forms.BookForm(request.POST or None)
        if book_form.is_valid():
            book_form.save()
            # book_form = forms.BookForm() # フォームを空に戻したい場合
        return render(request, 'index.html', context={
            'book_form': book_form
        })

class HomeView(TemplateView):

    template_name = 'home.html'

    #- context={'book_form': book_form}の代わりに用いる
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        print(kwargs) # {'name': '太郎'}
        #! データがからの場合、Noneを返し、エラーにならない
        context['name'] = kwargs.get('name')
        #! Noneの場合KeyErrorになる
        # context['name'] = kwargs['name']
        context['time'] = datetime.now()
        return context

class BookDetailView(DetailView):
    model = Books
    template_name = 'book.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        print(context)
        # context['form'] = forms.BookForm() #例
        return context

class BookListView(ListView):
    model = Books
    template_name='book_list.html'

    def get_queryset(self):
        # qs = super(BookListView, self).get_queryset()
        qs = super().get_queryset()
        qs = qs.order_by('-id')  # type: ignore
        qs = qs.order_by('description')  # type: ignore
        #- 動的に絞り込みを行う場合
        #- path('list_books/<name>', ~.as_view(), name='~'),
        #! self.kwargs で <name>を受け取ることができる!
        if 'name' in self.kwargs:
            qs = qs.filter(name__startswith='book')
        print(qs)
        print(dir(qs.first())) #pictures_setプロパティがあることを確認できる
        return qs

        # - 1行で書く場合
        return super().get_queryset().order_by('-id')

class BookCreateView(CreateView):
    model = Books
    fields = ['name', 'description', 'price']
    template_name = 'add_book.html'
    #- update成功時の遷移先を書いておかないとエラーが出る
    #- success_url or (Model)get_absolute_url
    #^ No URL to redirect to.  Either provide a url or define a get_absolute_url method on the Model.
    success_url = reverse_lazy('store:list_books')

    #- NOT NULL constraint failed: books.create_atを解消するため作成
    #- formの送信時の処理をカスタマイズする、送信前に実行される
    def form_valid(self, form):
        form.instance.create_at = datetime.now()
        form.instance.update_at = datetime.now()
        return super(BookCreateView, self).form_valid(form)

    def get_initial(self,**kwargs):
        initial = super().get_initial(**kwargs)
        initial['name'] = 'sample'
        return initial

class BookUpdateView(SuccessMessageMixin,UpdateView):

    template_name = "update_book.html"
    model = Books
    # fields = ['',''] # 入力するデータ or form_class = '' # 利用するFormを定義
    form_class = forms.BookUpdateForm
    #- SuccessMessageMixin
    success_message = '更新に成功しました'

    def get_success_url(self):
        print('self:', self) # self: <store.views.BookUpdateView object at 0x7fa56829a8b0>
        print(self.object) # Books object (3)
        #- reverse_lazyの挙動 要確認!
        #- 単純にリダイレクト先のURLを指定する。役割がredirect()と同じ
        #- kwargs={'pk': self.object.id}) or kwargs={'pk': self.kwargs['pk']}) どちらでも使えるが、wargs={'pk': self.kwargs['pk']})の場合のほうがエラーになりにくい
        # return reverse_lazy('store:edit_book', kwargs={'pk': self.object.id})
        return reverse_lazy('store:edit_book', kwargs={'pk': self.kwargs['pk']})

    def get_success_message(self, cleaned_data):
        print(cleaned_data) #{'name': 'book1-1', 'description': '心の旅2', 'price': 999}
        #- cleaned_data formの持っているデータを取得できる!
        return cleaned_data.get('name') + '更新しました'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        picture_form = forms.PictureUploadForm()
        #- 写真をtemplateに表示させるよう設定
        #- 現在更新中のオブジェクト(インスタンス)を取得 self.object or self.kwargs['pk']   キーワード引数
        pictures = Pictures.objects.filter_by_book(book=self.object)
        # pictures = Pictures.objects.filter_by_book(book=self.kwargs['pk'])
        context['pictures'] = pictures
        context['picture_form'] = picture_form
        return context

    def post(self, request, *args, **kwargs):
        # 画像をアップロードする処理を書く
        picture_form = forms.PictureUploadForm(request.POST or None, request.FILES or None)
        if picture_form.is_valid() and request.FILES:
            #-更新中のBookがどのBookなのか取得できる
            book = self.get_object()
            picture_form.save(book=book) #- kwargsの引数として渡している
        return super().post(request, *args, **kwargs)

class BookDeleteView(DeleteView):
    model = Books
    template_name = 'delete_book.html'
    success_url = reverse_lazy('store:list_books')

class BookFormView(FormView):

    template_name = 'form_book.html'
    form_class = forms.BookForm
    success_url = reverse_lazy('store:list_books')

    def get_initial(self): # Formの初期値を定義する
        initial = super(BookFormView, self).get_initial()
        initial['name'] = 'form sample'
        return initial

    def form_valid(self, form): # POST実行時の処理を定義する
        if form.is_valid():
            form.save()
        #- 下記の記述は定型文のようなもの - 覚える
        return super(BookFormView, self).form_valid(form)

class BookRedirectView(RedirectView):
    url = 'https://google.co.jp' # 静的に定義

    # 動的に定義
    def get_redirect_url(self, *args, **kwargs):
        book = Books.objects.first()
        print(book)
        if 'pk' in kwargs: # kwargsは /6 の部分
            #- http://127.0.0.1:8000/store/book_redirect_view/6 で検索するとhttp://127.0.0.1:8000/store/detail_book/6 に飛ぶ
            #^ path('book_redirect_view/<int:pk>', ~, ~'),
            return reverse_lazy('store:detail_book',kwargs={'pk':kwargs['pk']})

        #- http://127.0.0.1:8000/store/book_redirect_view で検索
        #^ <int:pk> の部分に kwargs={'pk':book.pk} が入る
        #^ path('edit_book/<int:pk>', ~, ~'),
        return reverse_lazy('store:edit_book', kwargs={'pk':book.pk})

def delete_picture(request, pk):
    picture = get_object_or_404(Pictures, pk=pk)
    # データベースからpicture情報を削除するが画像ファイルは残る
    picture.delete()
    #- 画像ファイル自体を削除
    import os
    if os.path.isfile(picture.picture.path):
        print('', picture.picture)
        print(picture.picture.path)
        os.remove(picture.picture.path)

    messages.success(request, '画像を削除しました')
    return redirect('store:edit_book', pk=picture.book.id)