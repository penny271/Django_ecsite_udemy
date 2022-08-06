from django.shortcuts import render
from . import forms

def index(request):
    return render(request, 'formapp/index.html')

def form(request):
    form = forms.UserInfo()
    return render(
        request, 'formapp/form_page.html', context={
            
        })