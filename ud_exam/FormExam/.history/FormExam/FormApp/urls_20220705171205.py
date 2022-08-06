from django.urls import path,include

urlpatterns = [
    path('insert_/', include('FormApp/urls.py')),
]