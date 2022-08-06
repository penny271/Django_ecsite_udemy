from pipes import Template
import django
from django.urls import path
#- class Based View(View) をimport
from .views import (
    IndexView, HomeView, BookDetailView,
    BookListView, BookCreateView, BookUpdateView,
    BookDeleteView,
)
#- Class Based View(TemplateView) ホーム画面など、シンプルなテンプレート画面を作成する際に用いる
# from django.views.generic.base import TemplateView
#- Class Based View(RedirectView) # 別のView, 別のページにリダイレクトをしたい場合に用いられる # urls.pyに直接定義するパターン
# from django.views.generic.base import RedirectView


app_name = 'store'

urlpatterns= [
    #- Viewを継承したIndexViewの as_view()メソッドを呼び出す
    path('index/', IndexView.as_view(), name='index'),
    #! views.pyを介さなくても静的なページにアクセスできる
    # path('home/', TemplateView.as_view(template_name='home.html'), name='home'),
    path('home/', HomeView.as_view(), name='home'),
    path('home/<name>', HomeView.as_view(), name='home'),
    #- # urls.py(pkで更新したいオブジェクトを取得する)
    path('detail_book/<int:pk>', BookDetailView.as_view(), name='detail_book'),
    path('list_books/', BookListView.as_view(), name='list_books'),
    #- 引数で絞り込む BookListView
    path('list_books/<name>', BookListView.as_view(), name='list_books'),
    path('add_book/', BookCreateView.as_view(), name='add_book'),
    path('edit_book/<int:pk>', BookUpdateView.as_view(), name='edit_book'),
    path('delete_book/,int:pk>', BookDeleteView.as_view(), name='delete_book')
    # path('delete_book/<int:pk>', BookDeleteView.as_view(), name='delete_book'),
    # path('book_form/', BookFormView.as_view(), name='book_form'),
    # path('google/', RedirectView.as_view(url='https://google.com')),
    # path('book_redirect_view/', BookRedirectView.as_view(), name='book_redirect_view'),
    # path('book_redirect_view/', BookRedirectView.as_view(), name='book_redirect_view'),
    # path('book_redirect_view/<int:pk>', BookRedirectView.as_view(), name='book_redirect_view'),
    # path('delete_picture/<int:pk>', delete_picture, name='delete_picture'),
]
