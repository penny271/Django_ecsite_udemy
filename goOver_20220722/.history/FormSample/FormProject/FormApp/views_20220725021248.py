from django.shortcuts import render
from django.forms import formset_factory, modelformset_factory
from . import forms
from .models import ModelSetPost

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
            #     f'name: {form.cleaned_data["name"]}, mail: {form.cleaned_data["mail"]}, a ge: {form.cleaned_data["age"]}'
            # )
            print(form.cleaned_data)


    return render(
        request, 'formapp/form_page.html', context={
            'form':form,
        })

def form_post(request):
    form = forms.PostModelForm()
    if request.method =='POST':
        form = forms.PostModelForm(request.POST)
        if form.is_valid():
            form.save()
    return render(request, 'formapp/form_post.html', context={'form':form})

def form_set_post(request):
    TestFormset = formset_factory(forms.FormSetPost,extra=3)
    formset = TestFormset(request.POST or None)
    if formset.is_valid():
        for form in formset:
            print(form.cleaned_data)
    return render(
        request, 'formapp/form_set_post.html',
        context={'formset': formset}
    )

def modelform_set_post(request):
    # TestFormSet = modelformset_factory(ModelSetPost, fields='__all__', extra=3)
    TestFormSet = modelformset_factory(ModelSetPost, form=forms.ModelFormSetPost, extra=3)
    formset = TestFormSet(request.POST or None, queryset=ModelSetPost.objects.filter(id__gt=3))
    if formset.is_valid():
        formset.save()
    return render(request, 'FormApp/modelform_set_post.html', context={'formset':formset})

def upload_sample(request):
    if request.method == 'POST' and request.FILES['uplaod_file']:
        upload_file = request.FILES['upload_file']
        fs = 

