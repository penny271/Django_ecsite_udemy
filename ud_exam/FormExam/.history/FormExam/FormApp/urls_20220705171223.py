from django.urls import path,include

urlpatterns = [
    path('insert_student/', include('FormApp/urls.py')),
]