
from django.urls import path,include

urlpatterns = [
    path('admin/', include('FormApp/urls.py')),
]