from django.shortcuts import render

# Create your views here.
def index(request):
    val = 'Good Bye'
    return render(request, 'index.html', context={'value':val})

def home(request):
    