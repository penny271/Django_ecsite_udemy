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

# Create your views here.

# def insert_student(request):
#     #! request.FILESも入れる
#     insert_form = forms.StudentInsertForm(request.POST or None, request.FILES or None )
#     if insert_form.is_valid():
#         insert_form.save()
#         #- 送信後、初期化 inputの中身を空にする
#         insert_form = forms.StudentInsertForm()
#     return render(request, 'form_app/insert_student.html', context={
#         'insert_form' : insert_form,
#     })


def insert_student(request):
    insert_form = forms.StudentInsertForm(request.POST or None, request.FILES or None )
    if insert_form.is_valid():
        insert_form.save()
        #- 初期化
        insert_form = forms.StudentInsertForm()
    return render(request, 'form_app/insert_student.html', context={
        'insert_form':insert_form
    })



#- Student情報を全件リスト表示する .modelsからStudentsを読み込む import
# def students_list(request):
#     students = Students.objects.all()
#     return render(
#         request, 'form_app/students_list.html', context={
#             'students':students,
#         }
#     )

def student_list(request):
    students = Students.objects.all()
    return render(request, 'form_app/student_list', context={ 'students': students})

# def update_student(request, id):
#     student = Students.objects.get(id=id)
#     #- インスタンス化
#     #- initialを使うことによってテーブルに保存されている内容を取得している
#     #- StudentUpdateForm(forms.Form): インスタンスを作り直している
#     update_form = forms.StudentUpdateForm(
#         initial={
#             'name': student.name,
#             'age': student.age,
#             'grade': student.grade,
#             'picture': student.picture,
#         }
#     )
#     if request.method == 'POST':
#         #- or の用法 左のものがなかったら右のものを入れる
#         update_form = forms.StudentUpdateForm(request.POST or None, request.FILES or None)
#         if update_form.is_valid():
#             #- studentはすでに id で一つに特定されている
#             #* cleaned_dataで入力された値を取り出している
#             student.name = update_form.cleaned_data['name']
#             student.age = update_form.cleaned_data['age']
#             student.grade = update_form.cleaned_data['grade']
#             #! pictureは追加の処理が必要 pictureの保存
#             picture = update_form.cleaned_data['picture']
#             if picture:
#                 fs = FileSystemStorage()
#                 file_name = fs.save(os.path.join('student', picture.name), picture)
#                 #- データベース内のstudent.picture をupdateしている
#                 student.picture = file_name
#             print('\n','student情報(update_form.cleaned_data): ', update_form.cleaned_data)
#             student.save()
#     return render(request, 'form_app/update_student.html', context={
#         'update_form':update_form,
#         'student':student
#     })


def update_student(request, id):
    #- 編集する特定のstudentを取得
    #- importすることで どの関数からでも指定のテーブルの情報にアクセスできる
    student = Students.objects.get(id=id)
    #- インスタンス化 - テーブルに保存されている値を初期値として表示
    update_form = forms.StudentUpdateForm( initial= {
        'name': student.name,
        'age': student.age,
        'grade': student.grade,
        'picture': student.picture,
    })
    if request.POST == 'POST':
        #---- 更新したい情報をインスタンス化
        update_form = forms.StudentUpdateForm(request.POST or None, request.FILES or None)
        if update_form.is_valid():
            student.name = update_form.cleaned_data['name']
            student.age = update_form.cleaned_data['age']
            student.grade = update_form.cleaned_data['grade']
            picture = update_form.cleaned_data['picture']
            if picture:
                fs = FileSystemStorage()
                file_name = fs(os.join.path('student',picture.name), picture)
                student.picture = file_name
            student.save()
    return render(request, 'form_app/update_student', context={'update_form': update_form,'student':student})


#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

# def delete_student(request, id):
#     delete_form = forms.StudentDeleteForm(
#         initial = {
#             'id':id,
#         }
#     )
#     if request.method == 'POST':
#         delete_form = forms.StudentDeleteForm(request.POST or None)
#         if delete_form.is_valid():
#             #- from .models import Students のidが一致する行を指定し、削除
#             Students.objects.get(id=delete_form.cleaned_data['id']).delete() #! データは消えるが、保存した画像ファイルは残ってしまう
#     return render(request, 'form_app/delete_student.html', context={
#         'delete_form':delete_form,
#     })

#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
def delete_student(request, id):
    # student = Students.objects.get('id = id')
    # delete_form = forms.StudentDeleteForm(initial={
        'id' = id   })
    update_form = forms.StudentUpdateForm( initial= {
        'name': student.name,
        'age': student.age,
        'grade': student.grade,
        'picture': student.picture,
    })


def insert_multiple_students(request):
    #- インスタンス化するための前段階
    #^ 第一引数にテーブル、第二引数にフィールド
    StudentFormSet = modelformset_factory(Students, fields='__all__', extra=3)
    #- インスタンス化
    insert_form = StudentFormSet(request.POST or None, request.FILES or None)
    if insert_form.is_valid():
        insert_form.save()
    return render(request, 'form_app/insert_multiple_students.html',context={'insert_form': insert_form})