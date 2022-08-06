
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
