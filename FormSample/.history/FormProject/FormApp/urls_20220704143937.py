from django.urls import path
from . import views

app_name=0 'form'

url_patterns = [
    path('', views.form_page)
]