from django.shortcuts import render

# Create your views here.
def index(request):
    val = 'Good Bye'
    return render(request, 'index.html', context={'value':val})

def home(request):
    # my_name = f'{first_name} {last_name}'
    my_name = '田中 次郎'
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
    return render('sample1/')