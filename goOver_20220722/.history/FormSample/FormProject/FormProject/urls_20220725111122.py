
from django.contrib import admin
from django.urls import path,include
#- 写真のurlをクリックして開けるようにする
#! FormProject の urls.py で記載するべきだったのに、
#! FormAppの urls.py に記載して時間を大幅に無駄にした
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    #- include()の中身は '' でくくる必要あり!
    path('form_app/',include('FormApp.urls'))
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

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