from pipes import Template
import django
from django.urls import path
#- class Based View(View) をimport
from .views import (
    IndexView, HomeView, BookDetailView,
    BookListView, BookCreateView, BookUpdateView,
    BookDeleteView, BookFormView, BookRedirectView,
)
#- Class Based View(TemplateView) ホーム画面など、シンプルなテンプレート画面を作成する際に用いる
# from django.views.generic.base import TemplateView
#- Class Based View(RedirectView) # 別のView, 別のページにリダイレクトをしたい場合に用いられる # urls.pyに直接定義するパターン
from django.views.generic.base import RedirectView

app_name = 'store'

urlpatterns= [
    #- Viewを継承したIndexViewの as_view()メソッドを呼び出す
    path('index/', IndexView.as_view(), name='index'),
    #! views.pyを介さなくても静的なページにアクセスできる
    path('home/<name>', HomeView.as_view(), name='home'),
    # #- # urls.py(pkで更新したいオブジェクトを取得する)
    path('detail_book/<int:pk>', BookDetailView.as_view(), name='detail_book'),
    path('list_books/', BookListView.as_view(), name='list_books'),
    #- 引数で絞り込む BookListView
    path('list_books/<name>', BookListView.as_view(), name='list_books'),
    path('add_book/', BookCreateView.as_view(), name='add_book'),
    path('edit_book/<int:pk>', BookUpdateView.as_view(), name='edit_book'),
    path('delete_book/<int:pk>', BookDeleteView.as_view(), name='delete_book'),
    path('book_form/', BookFormView.as_view(), name='book_form'),
    path('google/', RedirectView.as_view(url='https://google.com')),
    path('book_redirect_view/', BookRedirectView.as_view(), name='book_redirect_view'),
    path('book_redirect_view/<int:pk>', BookRedirectView.as_view(), name='book_redirect_view'),
    # path('delete_picture/<int:pk>', delete_picture, name='delete_picture'),
]


import os

TEMPLATE_DIR  = os.path.join(BASE_DIR, 'templates') #- 'DIRS': [], に TEMPLATE_DIRを追加する
STATIC_DIR = os.path.join(BASE_DIR, 'static')

STATICFILES_DIRS = (
    STATIC_DIR,
)

#- lec98 staticフォルダに識別子を加える事ができる
STATICFILES_DIRS = [
    ('download', STATIC_DIR),
]

#- ファイルのアップロード - ファイルの保存先の設定
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

#- プロジェクトフォルダ内のurls.py
from django.contrib import admin
from django.urls import path, include
# 写真を表示させる設定
from django.conf import settings
from django.conf.urls.static import static
# エラーメッセージページimport
# from accounts.views import show_error_page

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('boards/', include('boards.urls')),
]
#- エラーメッセージの処理 - lec212
# handler404 = show_error_page

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT )

#- 以下、画像用template
  <body>
    <form method='POST' enctype='multipart/form-data'>
      {% csrf_token %}
      <input type='file' name='upload_file'><br>
      <input type='submit' value='保存'>
    </form>

    {% if uploaded_file_url %}
    <p>保存先: <a href='{{ uploaded_file_url }}'>{{ uploaded_file_url }}</a></p>
    {% endif %}
  </body>