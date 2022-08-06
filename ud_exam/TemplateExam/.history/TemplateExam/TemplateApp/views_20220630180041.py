from django.shortcuts import render

# Create your views here.

class Member:

    def __init__(self,id,name,join_at,picture_path):
        self.id = id
        self.name = name
        self.join_at = join_at
        self.picture_path = picture_path

member_list = [
    Member(0, 'Taro', '2018/04/01', 'img/taro.jpg'),
    Member(1, 'Jiro', '2019/04/01', 'img/jiro.jpg'),
    Member(2, 'Hanako', '2019/05/01', 'img/hanako.jpg'),
    Member(0, 'Hanako', '2019/05/01', 'img/hanako.jpg'),
]

# ホーム画面
def home(request):
    return render(request, 'home.html')

# メンバー一覧
def members(request):
    pass