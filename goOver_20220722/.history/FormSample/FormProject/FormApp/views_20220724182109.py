from django.shortcuts import render
from . import forms

def index(request):
    return render(request, 'formapp/index.html')

def form_page(request):
    form = forms.UserInfo()
    if request.method == 'POST':
        #  Formで送られたデータを取り出す処理
        form = forms.UserInfo(request.POST)
        if form.is_valid():
            print('validation成功')
            # print(
            #     f'name: {form.cleaned_data["name"]}, mail: {form.cleaned_data["mail"]}, age: {form.cleaned_data["age"]}'
            # )
            print(form.cleaned_data)


    return render(
        request, 'formapp/form_page.html', context={
            'form':form,
        })

def form_post(request):
    form = forms.PostModelFrom(request.POST or None)
    return render(request, 'form_')

