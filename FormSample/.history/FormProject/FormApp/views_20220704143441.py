from django.shortcuts import render
from . import forms
# Create your views here.

def index(request):
    return render(request, 'formapp/index.html')

def form_page(request):
    #- forms.py から userInfoをインスタン化する
    form = forms.UserInfo()
