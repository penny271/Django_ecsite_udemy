from django.shortcuts import render

# Create your views here.
def user_list(request):
    return render(request, 'user/user_list.html', context={})

def index(request):
    