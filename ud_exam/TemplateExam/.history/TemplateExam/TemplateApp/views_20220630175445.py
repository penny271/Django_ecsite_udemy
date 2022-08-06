from django.shortcuts import render

# Create your views here.

# ホーム画面
def home(request):
    return render(request, 'home.html')