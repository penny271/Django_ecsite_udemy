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
        form = forms.UserInfo(request.POST)
        if form.is_valid():# バリデーション(フィールドが正しいかチェック)
            print('バリデーション成功')
            # print(f'name: {form.cleaned_data["name"]},mail: {form.cleaned_data["mail"]} age: {form.cleaned_data["age"]}')
            print(form.cleaned_data)
        #! invalidでもPOSTでフォームのデータは渡ってくる
        else:
            print('invalid form')
    return render(
        request, 'formapp/form_page.html', context={
            'form': form,
        }
    )

def form_page(request):
    form = forms.UserInfo()

    if request.method == 'POST':
        print(form.cleaned_data)
    else
