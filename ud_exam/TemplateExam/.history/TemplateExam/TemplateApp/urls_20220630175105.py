from django.urls import path
from . import views

urlpatterns = [
    path('app/', 'include('TemplateApp.urls'')),
]
