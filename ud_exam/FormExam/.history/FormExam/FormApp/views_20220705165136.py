from django.shortcuts import render
#- forms を使えるようにする - forms.pyの情報がmodels.pyを更新したものだから
from .import forms

# Create your views here.




def insert_student(request):
    form = forms.StudentInsertForm(request.POST or None )
    form = form(request.POST or None )