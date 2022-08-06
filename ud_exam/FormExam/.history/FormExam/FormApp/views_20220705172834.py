from django.shortcuts import render
#- forms を使えるようにする - forms.pyの情報がmodels.pyを更新したものだから
from .import forms

# Create your views here.




def insert_student(request):
    #! request.FILESも入れる
    insert_form = forms.StudentInsertForm(request.POST or None, request.FILES or None )
    if insert_form.is_valid():
        insert_form.save()
        #- 送信後、初期化
        insert_form = forms.StudentInsertForm()
    return render(request, 'form_app/insert_student.html', context={
        'insert_form' : insert_form,
    })