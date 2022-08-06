
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
    path('formapp')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)