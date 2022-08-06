from django.urls import path
from . import views


app_name = 'first_app'

urlpatterns = [
    path('a', views.index, name = 'index')
]

