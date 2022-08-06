from django.shortcuts import render

# Create your views here.
def index(request):
    val = 'Good Bye'
    # templates/index.htmと記載する必要なし 省略可能
    return render(request, 'index.html', context={'value':val})

def home(request):
    my_name = 'Taro Yamada'
    favorite_fruits = ['Apple', 'Grape', 'Lemon']
    my_info = {
        'name': 'Taro',
        'age'
    }