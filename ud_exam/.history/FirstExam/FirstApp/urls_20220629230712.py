from django.urls import path
from . import views


app_name = 'first'

urlpatterns = [
    # path('hello', views.index, name = 'index'),
    # #- <str:user_name>これが views.pyの中のuser_page関数の引数となる
    # path('page/<str:user_name>', views.user_page, name='user_page'),
    # # path('page/user_name', views.user_page, name='user_page'),
    # path('number_page/<str:user_name>/<int:number>',views.number_page, name='number_page'),
    path('add/<int:num1>/<int:num2>',views.add, name = 'add'),
    path('minus/<str:num1>/<str:num2>',views.minus, name = 'minus'),
    path('div/<str:num1>/<str:num2>',views.div, name = 'div'),
]


urlpatterns = [
    path('add/<int:num1>/<int:num2>')
]