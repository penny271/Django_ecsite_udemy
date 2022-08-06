from django.shortcuts import render
from . import forms

def index(request):
    return render(request, 'formapp/index.html')

def form_page(request):
    form = forms.UserInfo()
    if request.(self, *args, **kwargs):
        return super().(*args, **kwargs)


    return render(
        request, 'formapp/form_page.html', context={
            'form':form,
        })