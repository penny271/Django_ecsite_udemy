from django.shortcuts import render
from user.forms import 

# Create your views here.
def user_list(request):
    return render(request, 'user/user_list.html', context={})

def index(request):
    return render(request, 'user/index.html')

def register(request):
    user_form = UserForm