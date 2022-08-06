from django.urls import path
from . import views

#- app_name 重要!!
#- htmlファイル内で {% url 'form_app:insert_student'} のように使用する
app_name = 'form_app'

urlpatterns = [
    path('insert_student/', views.insert_student, name='insert_student'),
    path('students_list/', views.students_list, name='students_list'),
    # path('update_student/', views.update_student, name='update_student'),
    #- idを渡す
    path('update_student/<int:id>', views.update_student, name='update_student'),
]