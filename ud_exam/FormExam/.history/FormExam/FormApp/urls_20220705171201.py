from django.urls import path,include

urlpatterns = [
    path('insert/', include('FormApp/urls.py')),
]