from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse('<h1>Good bye</h1>')

# def user_page(request, user_name):
#     return HttpResponse(f'<h1>{user_name}\'s page</h1>')

# # 複数の引数可能
# def number_page(request, user_name, number):
#     user_name = user_name.upper()
#     return HttpResponse(f'<h1>{user_name}\'s page number = {number}</h1>')

def add(request, num1, num2):
    return HttpResponse(f'<h1>{num1 + num2}</h1>')

def minus(request, num1, num2):
    num1 = float(num1)
    num2 = float(num2)
    return HttpResponse(f'<h1>{num1 - num2}</h1>')

def div(request, num1, num2):
    num1 = float(num1)
    num2 = float(num2)
    roundup_num = round(num1 + num2)
    return HttpResponse(f'<h1>{num1 + num2}</h1>')