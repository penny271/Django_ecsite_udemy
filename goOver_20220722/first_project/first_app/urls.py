from django.urls import path
# from .views import index
from . import views
# import views #! 不可 なぜかはわからない

app_name = 'first_app'

urlpatterns = [
    # path('hello', index, name='index'),
    path('hello', views.index, name='index'),
    path('user_page/<str:user_name>', views.user_page, name='user_page'),
    path('number_page/<str:user_name>/<int:number>', views.number_page, name='number_page'),
]