from django.urls import path
from djan.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('app/', include('TemplateApp.urls')),
]
