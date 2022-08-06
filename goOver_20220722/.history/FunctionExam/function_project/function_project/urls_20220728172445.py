
from django.contrib import admin
from django.urls import path, include
#- 写真を表示させる設定
from django.conf import settings
from django.conf.urls.static import static
# #- エラーメッセージページimport
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