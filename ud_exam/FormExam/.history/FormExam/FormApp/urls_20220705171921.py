from django.urls import path
from . import views

#- app_name 重要!!
#- {% url 'form_app:insert_student'} などで使用する
app_name = 'form_app'

urlpatterns = [
    path('insert_student/', views.insert_student, name='insert_student'),
]