from django.shortcuts import render

# Create your views here.
def index(request):
    val = 
    # templates/index.htmと記載する必要なし 省略可能
    return render(request, 'index.html', context={'value':'Hello'})