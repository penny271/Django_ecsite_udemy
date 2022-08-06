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

# class UserLoginView(FormView):
#     template_name = 'user_login.html'
#     form_class = UserLoginForm

#     #- データの受取用 POSTが必要
#     def post(self, request, *args, **kwargs):
#         email = request.POST['email']
#         password = request.POST['password']
#         user = authenticate(email=email, password=password)
#         #- url上のnext=/accounts/user/を取得
#         next_url = request.POST['next']
#         print(next_url)
#         if user is not None and user.is_active:
#             login(request,user)
#         if next_url:
#             return redirect(next_url) # この場合は'accounts:user'に飛ぶ
#         return redirect('accounts:home')

#- (LoginView)を使うと、next=/accounts/user/ の
class UserLoginView(LoginView):
    template_name = 'user_login.html'
    authentication_form = UserLoginForm

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

class UserLogoutView(View):
    def get(self, request, *args, **kwargs):
        logout(request)
        return redirect('accounts:user_login')

#^ settings.pyにログインしていない場合のリダイレクト先を設定する。
#^ 例: LOGIN_URL = '/accounts/user_login'
#- ログインが必要なViewにデコレータを付ける方法
# @method_decorator(login_required, name='dispatch')
# class UserView(LoginRequiredMixin,TemplateView):
#     template_name = 'user.html'
#     print('A')

#     #- dispatchは必ず実行されるメソッド
#     # @method_decorator(login_required)
#     def dispatch(self,  *args, **kwargs):
#         print('dispatch')
#         return super().dispatch( *args, **kwargs)

#- settings.py に LOGIN_URL = '/accounts/user_login' を要設定 or エラー発生 redirect先
# @method_decorator(login_required, name='dispatch')
class UserView(LoginRequiredMixin,TemplateView):

    template_name = 'user.html'

    #- GETまたはPOSTの処理を受け渡されたrequestに応じて行うメソッド いずれの場合も必ず実行される dispatch()
    # @method_decorator(login_required)
    def dispatch(self,  *args, **kwargs):
        return super().dispatch( *args, **kwargs)
