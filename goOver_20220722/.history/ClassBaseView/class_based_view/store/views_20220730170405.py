from datetime import datetime
from django.shortcuts import render
from django.views.generic.base import (
    View, TemplateView, RedirectView
)
from django.views.generic.detail import DetailView

from .models import Books
from . import forms
from datetime import datetime

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
    template