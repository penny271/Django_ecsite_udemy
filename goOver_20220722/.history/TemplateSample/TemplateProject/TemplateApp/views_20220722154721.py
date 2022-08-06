from django.shortcuts import render

# Create your views here.
def index(request):
    val = 'Good Bye'
    return render(request, 'index.html', context={'value':val})

def home(request, first_name, last_name):
    my_name = f'{first_name} {last_name}'
    favorite_fruits = ['Apple', 'Grape', 'Lemon']
    my_info = {
        'name': 'Taro',
        'age':18,
    }
    return render(request, 'home.html', context={
        'my_name': my_name,
        'my_name': my_name,
        'my_name': my_name,
        'my_name': my_name,

    })