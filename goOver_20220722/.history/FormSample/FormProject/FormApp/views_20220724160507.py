from django.shortcuts import render
from . import forms

def index(request):
    return render(request, 'form')