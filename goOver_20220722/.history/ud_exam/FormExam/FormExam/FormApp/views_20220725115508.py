from django.shortcuts import render
#- forms を使えるようにする - forms.pyの情報がmodels.pyを更新したものだから
from . import forms
from .models import Students
#- media保存関連
from django.core.files.storage import FileSystemStorage
import os
#- データの一括登録方法に必要
from django.forms import modelform_factory, modelformset_factory

def insert_student_form(request):
    student = forms.StudentInsertForm