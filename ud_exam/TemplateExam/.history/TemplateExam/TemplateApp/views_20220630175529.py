from django.shortcuts import render

# Create your views here.

class Member:

    def __init__

# ホーム画面
def home(request):
    return render(request, 'home.html')

# メンバー一覧
def members(request):
    pass