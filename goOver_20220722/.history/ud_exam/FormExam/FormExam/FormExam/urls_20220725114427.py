from django.contrib import admin
from django.urls import path, include
#- 画像を表示できる用に設定
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    #! 'FormApp/urls' と書いていたが、正しくは FormApp.urls
    #! NG =>  path('form_app/', include('FormApp/urls')),
    path('form_app/', include('FormApp.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
