from django.shortcuts import render

# Create your views here.
def index(request):
    val = '変数です'
    return render(request, 'index.html', context={'value':'Hello'})