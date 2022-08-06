from django.shortcuts import render

# Create your views here.
def index(request):
    val = 'Good Bye'
    # templates/index.htmと記載する必要なし 省略可能
    return render(request, 'TemplateApp/index.html', context={'value':val})

def home(request):
    my_name = 'Taro Yamada'
    favorite_fruits = ['Apple', 'Grape', 'Lemon']
    my_info = {
        'name': 'Taro',
        'age':18,
    }
    return render(request, 'home.html', context={
        'my_name': my_name,
        'favorite_fruits': favorite_fruits,
        'my_info': my_info,
    })

def sample1(request):
    return render(requ)