from django.urls import path
from . import views

app_name= 'form_app'

url_patterns = [
    path('', views.form_page)
]