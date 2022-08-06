from django.shortcuts import render
#- forms を使えるようにする - forms.pyの情報がmodels.pyを更新したものだから
from . import forms
from .models import Students
#- media保存関連
from django.core.files.storage import FileSystemStorage
import os
#- データの一括登録方法に必要
from django.forms import modelform_factory, modelformset_factory

def insert_student(request):
    insert_form = forms.StudentInsertForm(request.POST or None, request.FILES or None)
    if insert_form.is_valid():
        insert_form.save()
        insert_form = forms.StudentInsertForm() # inputの初期化
    return render(request,'form_app/insert_student.html', context={
        'insert_form': insert_form
    })

def students_list(request):
    students = Students.objects.all()
    return render(request, 'form_app/students_list.html', context={
        'students': students
    })

def update_student