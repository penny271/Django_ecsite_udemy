from django.shortcuts import render
#- forms を使えるようにする - forms.pyの情報がmodels.pyを更新したものだから
from .import forms

# Create your views here.




def insert_student(request):
    #! request.FILESも入れる
    insert_form = forms.StudentInsertForm(request.POST or None, request.FILES or None )
    if insert_form.is_valid():
    if request.method == 'POST':
        insert_form.save()
    return render(request, 'FormApp/insert_student.html', context={
        'insert_form' : insert_form,
    })