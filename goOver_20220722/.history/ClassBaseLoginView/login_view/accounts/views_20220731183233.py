from readline import parse_and_bind
from django.shortcuts import render,redirect
from django.views.generic.edit import CreateView, FormView
from django.views.generic.base import TemplateView, View
from .forms import RegistForm, UserLoginForm
from django.contrib.auth import authenticate, login, logout
#- Class Based View(LoginRequiredMixin)
#- ログインが必要なViewに付与するLoginRequiredMixinやmethod_decoratorを用いる
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.auth.mixins import LoginRequiredMixin
#- Class Based View(LoginView, LogoutView)
from django.contrib.auth.views import LoginView,LogoutView


# Create your views here.

class HomeView(TemplateView):
    template_name = 'home.html'

class RegistUserView(CreateView):
    template_name = 'regist.html'
    form_class = RegistForm

class UserLoginView(FormView):
    template_name = 'user_login.html'
    form_class = UserLoginForm

    #- データの受取用 POSTが必要
    def post(self, request, *args, **kwargs):
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(emai=email, password=password)
        if user is not None and user.is_active:
            login(request,user)
        return redirect('accounts:home')

# class UserLoginView(LoginView):
#     template_name = 'user_login.html'
#     authentication_form = UserLoginForm

#     #- # This method is called when valid form data has been POSTed.
#     def form_valid(self, form):
#         remember = form.cleaned_data['remember']
#         #-セッションの保存時間を引数の時間(秒)に変更する。引数が0の 場合、ブラウザを閉じるとセッションがなくなる。もし value が datetime または timedelta オブジ ェクトならば、指定された日時に破棄される
#         if remember:
#             self.request.session.set_expiry(1200000)
#         return super().form_valid(form)

# class UserLogoutView(View):

#     def get(self, request, *args, **kwargs):
#         logout(request)
#         return redirect('accounts:user_login')

class UserLogoutView(LogoutView):
    def get(self, request, *args, **kwargs):
        
        return super().get(request, *args, **kwargs)

#^ djangoのヴァージョンアップでログインしていない場合は設定なしで
#^ ログイン画面へ飛ばす仕様になっている模様。
#- ログインが必要なViewにデコレータを付ける方法
# @method_decorator(login_required, name='dispatch')
class UserView(LoginRequiredMixin,TemplateView):
    template_name = 'user.html'
    print('A')

    #- dispatchは必ず実行されるメソッド
    # @method_decorator(login_required)
    def dispatch(self,  *args, **kwargs):
        print('dispatch')
        return super().dispatch( *args, **kwargs)
