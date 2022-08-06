from django.shortcuts import render
from . import forms

def index(request):
    return render(request, 'formapp/index.html')

def form(request):
    return render(request, 'formapp/form.html')