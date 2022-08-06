from django.urls import path
from .views import (ProductListView,)

app_name='stores'

urlpatterns = [
    path('product_list', ProductListView.as_view(), name='procut_list')
]
