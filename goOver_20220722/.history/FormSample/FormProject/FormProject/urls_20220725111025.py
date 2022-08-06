
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

    #- ★★project内のurls.pyに記載する!!!!!!! アプリ内ではない!!
from django.conf import settings
from django.conf.urls.static import static

# urlpatterns の下に記載する
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# mediaフォルダを作成する
# その中に、 models.pyで記述した upload_to='xxx' の xxxフォルダを作成する

#html内 enctype="multipart/form-data"
<form method="POST" enctype="multipart/form-data" >
</form>