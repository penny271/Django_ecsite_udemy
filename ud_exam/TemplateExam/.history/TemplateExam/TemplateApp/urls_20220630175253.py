from django.urls import path
from . import views

app_bame = 'app'
urlpatterns = [
    path('home/', views.home, name='home'),
    path('members/', views.members, name='members'),
]
