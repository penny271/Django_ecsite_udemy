from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from allauth.socialaccount.providers.google.urls import urlpatterns as google_url

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('oauth_accounts/', include('allauth.urls')),
    path('oauth_accounts/', include(google_url)),
    path('accounts/', include('accounts.urls')),
    path('stores/', include('stores.urls')),
]

# urlpatterns の下に記載する
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)