from django.shortcuts import render
from django.urls import path
from . import views
from django.views import re

app_name = 'template_app'

urlpatterns = [
    path('', views.index, name = 'index'),
    #### path('home', views.home, name='home'),
    path('home', views.home, name='home'),


    # path('home /<first_name>/<last_name>', views.home, name='home'),
    path('sample1', views.sample1, name='sample1'),
    path('sample2', views.sample2, name='sample2'),
    # path('sample', views.sample, name='sample'),
    # path('sample3', views.sample3, name='sample3'),
]

def sample(request):
    name = 'ichiro yamada'
    height = 175.5
    weight = 72
    bmi = weight / (height / 100) **2
    page_url = 'ホームページ: https://www.google.com'
    favorite_fruits = ['Apple', 'Grape', 'Lemon']
    msg = """hello
    my name is
    ichiro
    """
    msg2 = '1234567890'
    return render(request, 'sample.html', context = {
        'name': name,
        'bmi': bmi,
        'page_url' : page_url,
        'fruits' : favorite_fruits,
        'msg': msg,
        'msg2': msg2
    })
