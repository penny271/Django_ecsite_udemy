from turtle import update
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

def update_student(request, id):
    student = Students.objects.get(id=id)
   #- インスタンス化 - テーブルに保存されている値を初期値として表示
    update_form = forms.StudentUpdateForm(
        initial={
            'name': student.name,
            'age': student.age,
            'grade': student.grade,
            'picture': student.picture,
        }
    )
    if request.method == 'POST':
        update_form = forms.StudentUpdateForm(request.POST or None, request.FILES or None)
        if update_form.is_valid():
            # update_form.save() #! 不可 forms.StudentUpdateForm()が forms.Formなので save()メソッドが使えない!!
            student.name = update_form.cleaned_data['name']
            student.age = update_form.cleaned_data['age']
            student.name = update_form.cleaned_data['name']
            student.name = update_form.cleaned_data['name']

    return render(
        request, 'form_app/update_student.html',context={
            'update_form': update_form,
            'student': student,
        }
    )