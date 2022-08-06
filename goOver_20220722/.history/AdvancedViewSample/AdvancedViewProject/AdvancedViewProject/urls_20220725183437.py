from django.contrib import admin
from django.urls import path,include
from store import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('store/', include('store.urls')),
    path('user/', include('user.urls')),
]

#-  特殊な変数 エラーハンドリング
#^ views.page_not_found関数にhandler404を設定する
handler404 = views.page_not_found
# handler500 = views.server_error
