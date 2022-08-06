from django.shortcuts import render, redirect
from django.http import HttpResponse
from user.forms import UserForm, ProfileForm, LoginForm
#- passwordが合っているか確認
#- login, logout
from django.contrib.auth import authenticate,login, logout
#- loginしているときのみ特定の関数を有効にする
from django.contrib.auth.decorators import login_required
#- passwordのvalidation
from django.contrib.auth.password_validation import validate_password
#- passwrodのvalidation時の例外対応
from django.core.exceptions import ValidationError

# Create your views here.
def user_list(request):
    return render(request, 'user/user_list.html', context={})

def index(request):
    return render(request, 'user/index.html')

def register(request):
    user_form = UserForm(request.POST or None)
    profile_form = ProfileForm(request.POST or None, request.FILES or None)
    if user_form.is_valid() and profile_form.is_valid():
        user = user_form.save()
        #- パスワードを暗号化して保存する
        user.set_password(user.password)
        user.save() # ユーザ保存
        profile = profile_form.save(commit=False)
        #- profileは user1対1で紐付いているので外部キーとしてユーザを登録できる
        profile.user = user
        profile.save()
    return render(request, 'user/registration.html', context={
        'user_form': user_form,
        'profile_form': profile_form
    })


def user_login(request):
    login_form = LoginForm(request.POST or None)
    if login_form.is_valid():
        username = login_form.













    #     username = login_form.cleaned_data.get('username')
    #     password = login_form.cleaned_data.get('password')
    #     #- passwordが合っているか確認 - importした関数使用
    #     user = authenticate(username=username, password=password)
    #     if user:
    #         #- userが有効な場合
    #         if user.is_active:
    #             login(request, user)
    #             return redirect('user:index')
    #         else:
    #             return HttpResponse('アカウントがアクティブでないです。')
    #     #- userが存在しない場合
    #     else:
    #         return HttpResponse('ユーザーが存在しません')
    # return render(request, 'user/login.html', context={
    #     'login_form':login_form,
    # })

#- loginしているときのみ特定の関数を有効にする
@login_required
def user_logout(request):
    logout(request)
    return redirect('user:index')

@login_required
def info(request):
    return HttpResponse('ログインしています')