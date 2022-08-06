from django.urls import path
from . import views

#- app_name 重要!! {}

urlpatterns = [
    path('insert_student/', views.insert_student, name='insert_student'),
]