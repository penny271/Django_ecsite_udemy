from datetime import datetime
from django import http
from django.shortcuts import render, redirect,  get_object_or_404
#- Class Based View(View)最も基本的なView (TemplateView) ホーム画面など、シンプルなテンプレート画面を作成する際に用いる / #- Class Based View(RedirectView) # 別のView, 別のページにリダイレクトをしたい場合に用いられる
from django.views.generic.base import (
    View, TemplateView, RedirectView
)
from django.views.bene
#- Class Based View(DetailView) 挿入したデータの詳細を表示
from django.views.generic.detail import DetailView
#- Class Based View(ListView) 挿入したデータの一覧を表示したい場合に用いる。
from django.views.generic.list import ListView
#- Class Based View(CreateView) 作成したテーブルにデータを挿入したい場合に用いる。/ Class Based View(UpdateView) 挿入したデータを更新したい場合に用いる。/ Class Based View(DeleteView) 挿入したデータを削除したい場合に用いる。 / Class Based View(FormView) 一般にFormを用いる場合使う。
from django.views.generic.edit import (
    CreateView,UpdateView, DeleteView, FormView
)
from . import forms
from datetime import datetime
from .models import Books, Pictures
#- django.urls.reverse_lazy # 関数名から、その関数を呼び出すパスを返す(success_url, get_absolute_urlに用いる)
from django.urls import reverse_lazy
#- データ更新時、削除時などにメッセージを表示するには、SuccessMessageMixinを用いると良い (django.contrib.messages.views.SuccessMessageMixin)
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
#- logging lec247
import logging
from django.http import Http404

#- settings.pyに記述したloggersの名前で使用できるようになる
application_logger = logging.getLogger('application-logger')
error_logger = logging.getLogger('error-logger')

class IndexView(View):

    def get(self, request, *args, **kwargs):
        book_form = forms.BookForm()
        return render(request, 'index.html',context={
            'book_form':book_form,
        })

    #- POSTメソッドを記述していないとsubmitした際にエラーになる
    def post(self, request, *args, **kwargs):
        book_form = forms.BookForm(request.POST or None)
        if book_form.is_valid():
            book_form.save()
        return render(request, 'index.html', context={
            'book_form': book_form,
        })

#- Class Based View(TemplateView)
class HomeView(TemplateView):

    template_name = 'home.html'

    #- path('home/<name>', HomeView.as_view(), name='home') の
    #- <name>が 引数 **kwargsの中に入る
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        application_logger.debug('Home画面を表示します')
        if kwargs.get('name') == 'ああああ':
            # error_logger.error('この名前は利用できません')
            raise Http404('この名前は使用できません')
            print('aaa')
        print(kwargs)
        context['name'] = kwargs.get('name')
        context['time'] = datetime.now()
        return context

#- Class Based View(DetailView) 挿入したデータの詳細を表示
class BookDetailView(DetailView):
    model = Books
    template_name= 'book.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        print(context)
        #- 例: forms.pyからもデータを持ってくることができる
        # context['form'] = forms.BookForm()
        return context

class BookListView(ListView):
    model = Books
    template_name = 'book_list.html'

    #- def get_queryset(self): # データを取得する際のSQLを定義する。
    def get_queryset(self):
        qs = super(BookListView,self).get_queryset()
        #- path('list_books/<name>', の <name>を持ってきている
        if 'name' in self.kwargs:
            # qs = qs.filter(name__startswith='book')
            qs = qs.filter(name__startswith=self.kwargs['name'])
        qs = qs.order_by('description') # 降順に並び替え
        print(qs)
        return qs

class BookCreateView(CreateView):
    model = Books
    fields = ['name', 'description', 'price']
    template_name = 'add_book.html'
    #- Create成功時の遷移先を定義する
    success_url = reverse_lazy('store:list_books')
    #^ or (Model)get_absolute_url = ‘’ を使う  #こちらは、対象のモデルに定義する ※療法記載がある場合、success_url が優先される

    #- フォーム送信前に実行されるメソッド
    #- def form_valid(self, form) # formの送信時の処理をカスタマイズする
    #! エラー: NOT NULL constraint failed: books.create_at
    #! を解消するために以下を付け加える
    def form_valid(self, form):
        form.instance.create_at = datetime.now()
        form.instance.update_at = datetime.now()
        return super(BookCreateView,self).form_valid(form)

    #- def get_initial(self, **kwargs): # 初期値を設定する
    def get_initial(self, **kwargs):
        initial = super(BookCreateView,self).get_initial(**kwargs)
        initial['name']='sample'
        return initial

#- SuccessMessageMixinをメッセージ出力のため多重継承させる
class BookUpdateView(SuccessMessageMixin, UpdateView):

    template_name = 'update_book.html'
    model = Books
    #- 下記のforms.BookUpdateFormで save()処理している
    form_class = forms.BookUpdateForm
    #- この後、詳細画面に移る
    #-  model側でdef get_absolute_url(self): を設定しているから

    #成功した場合のメッセージを定義(静的)
    success_message = '更新に成功しました。'

    def get_success_url(self): # 成功時の遷移先を定義する
        print(self.object) # Books object (4)
        return reverse_lazy('store:edit_book', kwargs={'pk':self.object.id})

    # 成功した場合のメッセージを定義(動的)
    def get_success_message(self, cleaned_data):
        print(cleaned_data)
        return cleaned_data.get('name') + 'を更新しました'

    #- # テンプレートに渡す値を指定する
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        picture_form = forms.PictureUploadForm()
        pictures = Pictures.objects.filter_by_book(book=self.object)
        #!!!!
        print('book=self.object:', self.object)
        print('pictures:', pictures)
        context['pictures'] = pictures
        context['picture_form'] = picture_form
        return context

    def post(self, request, *args, **kwargs):
        #  画像をアップロードする処理を書く
        picture_form = forms.PictureUploadForm(request.POST or None, request.FILES or None)
        if picture_form.is_valid() and request.FILES:
            #- 更新中のBookがどのBookなのか取得
            #! 外部キー
            book = self.get_object()
            #! forms.py でsave()内容を更新
            picture_form.save(book = book)


        return super(BookUpdateView, self).post(request, *args, *kwargs)

class BookDeleteView(DeleteView):
    model = Books
    template_name = 'delete_book.html'
    success_url = reverse_lazy('store:list_books')

class BookFormView(FormView):

    template_name = 'form_book.html'
    form_class = forms.BookForm
    success_url = reverse_lazy('store:list_books')

    def get_initial(self): # Formの初期値を定義する
        initial = super(BookFormView,self).get_initial()
        initial['name'] = 'form sample'
        return initial

    #- POST実行時の処理を定義する
    def form_valid(self, form):
        if form.is_valid():
            form.save()
        #- returnを返さなくてもsave()できるが、その後エラーになる
        return super(BookFormView, self).form_valid(form)

class BookRedirectView(RedirectView):
    url = 'https://yahoo.com'

    def get_redirect_url(self, *args, **kwargs):
        book = Books.objects.first()
        #- path('book_redirect_view/<int:pk>' の<int:pk>がkwargsにあたる
        if 'pk' in kwargs:
            return reverse_lazy('store:detail_book', kwargs={'pk':kwargs['pk']})
        print(book)
        return reverse_lazy('store:edit_book', kwargs={'pk': book.pk})


def delete_picture(request, pk):
    picture=get_object_or_404(Pictures, pk=pk)
    #! picture.delete() だけだとmedia/pictureの画像は消せない
    #! データベースとの紐付けだけが消える
    picture.delete()
    #- 下記をすることによって、画像ファイル自体を削除できる
    # import os
    # print(picture)
    # print(picture.picture)
    # print(picture.picture.path)
    # if os.path.isfile(picture.picture.path):
    #     os.remove(picture.picture.path)

    messages.success(request, '画像を削除しました')
    return redirect('store:edit_book', pk=picture.book.id)