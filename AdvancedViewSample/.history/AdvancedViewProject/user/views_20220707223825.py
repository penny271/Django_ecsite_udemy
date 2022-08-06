import profile
from django.shortcuts import render
from user.forms import UserForm, ProfileForm

# Create your views here.
def user_list(request):
    return render(request, 'user/user_list.html', context={})

def index(request):
    return render(request, 'user/index.html')

def register(request):
    user_form = UserForm(request.POST or None)
    profile_form = ProfileForm(request.POST or None, request.FILES or None)
    if user_form.is_valid() and profile_form.is_valid():
        user = user_form.save() #ユーザー登録
        user.set_password(user.password) #パスワードを暗号化して保存する
        user.save() #ユーザーを保存する
        #- データベースに保存ではなく、メモリ上に保存 commit=False
        profile = profile_form.save(commit=False)
        #! profileはuserと1対1で紐付いているので
        #! .userで設定すると外部キーとしてユーザーを登録することができる
        profile.user = user
        profile.save() #- ハードディスク上に保存
    return render(request, 'user/registration.html', context={
        'user_form':user_form,
        
    })