from django.shortcuts import render
from . import forms
# Create your views here.

def index(request):
    return render(request, 'formapp/index.html')

def form_page(request):
    #- forms.py から userInfoをインスタン化する
    form = forms.UserInfo()
    if request.method == 'POST':
        # Formで送られたデータを取り出す
        form = forms.UserInfo(request.Post)
        if form.is_valid():# バリデーション(フィールドが正しいかチェック)
    return render(
        request, 'formapp/form_page.html', context={
            'form': form,
        }
    )