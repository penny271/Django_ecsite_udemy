from django.urls import path
from . import views

app_name= 'form_app'

url_patterns = [
    path('', views.index, name='index'),
    #- path()の第一引数 / を最後に書く!! そうでないとエラーになる
    path('form_page/', views.form_page, name= 'form_page'),
]