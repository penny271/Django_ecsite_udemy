from django.urls import path
from . import views

app_name = 'user'

urlpatterns = [
    path('user_list', views.user_list, name='user_list'),
    path('index', views.index, name='index'),
    path('user_list', views.user_list, name='user_list'),

]