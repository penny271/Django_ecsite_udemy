from datetime import datetime
from django.shortcuts import render
from django.views.generic.base import (
    View, TemplateView, RedirectView
)
from . import forms

class IndexView(View):

    def get(self, request, *args, **kwargs):
        book_form = forms.BookForm()
        return render(request, 'index.html', context={
            'book_form': book_form
        })

    def post(self, request,*args, **kwargs):
        book_form = forms.BookForm(request.POST or None)
        if book_form.is_valid():
            book_form.save()
        return render(request, 'store/index.html', context={
            'book_form': book_form
        })
