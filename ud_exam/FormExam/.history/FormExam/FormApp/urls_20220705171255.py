from django.urls import path,include
from . import views

urlpatterns = [
    path('insert_student/', views.insert_student, name='insert_student'),
]