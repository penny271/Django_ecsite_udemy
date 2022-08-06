from django.urls import path
from . import views

app_name = 'template_app'

urlpatterns = [
    path('', views.index, name = 'index'),
    path('home', views.home, name='home'),
    path('home', views.home, name='home'),
    path('home', views.home, name='home'),
]