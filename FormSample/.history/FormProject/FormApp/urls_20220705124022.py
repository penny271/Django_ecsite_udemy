from django.urls import path
from . import views
#- 写真のurlをクリックして開けるようにする
from django.conf import settings
from django.conf.urls.static import static

from django.conf import settings
from django.conf.urls.static import static

app_name= 'form_app'

#! urlpatternsと書くべきところを url_patterns と記載しており、うまくいかなかった -20220704
# url_patterns = [
urlpatterns = [
    path('', views.index, name='index'),
    #- path()の第一引数 / を最後に書く!! そうでないとエラーになる
    path('form_page/', views.form_page, name= 'form_page'),
    path('form_post/', views.form_post, name= 'form_post'),
    path('form_set_post/', views.form_set_post, name= 'form_set_post'),
    path('modelform_set_post/', views.modelform_set_post, name= 'modelform_set_post'),
    path('upload_sample/', views.upload_sample, name= 'upload_sample'),
]

if settings.DEBUG:
    # urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

    print('urlpatterns'.urlpatterns)


# urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)