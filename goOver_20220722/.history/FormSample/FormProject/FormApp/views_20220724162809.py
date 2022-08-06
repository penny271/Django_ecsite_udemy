from django.shortcuts import render
from . import forms

def index(request):
    return render(request, 'formapp/index.html')

def form_page(request):
    form = forms.UserInfo()
    if request.method == 'POST':
        #  Formで送られたデータを取り出す処理
        form = forms.UserInfo

    return render(
        request, 'formapp/form_page.html', context={
            'form':form,
        })