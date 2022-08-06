from django.urls import path
from . import views


app_name = 'first_app'

urlpatterns = [
    path('s', views.index, name = 'index')
]

