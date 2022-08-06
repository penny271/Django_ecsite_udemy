from django.shortcuts import render

# Create your views here.

class Member:

    def __init__(self,id,name,join_at,picture_path):
        self.id = id
        self.name = name
        self.join_at = join_at
        self.id = id

# ホーム画面
def home(request):
    return render(request, 'home.html')

# メンバー一覧
def members(request):
    pass