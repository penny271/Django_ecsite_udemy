from django.urls import path
from .views import (
    ProductListView, Product_DetailView, add_product,
)

app_name='stores'

urlpatterns = [
    path('product_list', ProductListView.as_view(), name='product_list'),
    path('product_detail/<int:pk>', Product_DetailView.as_view(), name='product_detail'),
    path('product_detail/<int:pk>', Product_DetailView.as_view(), name='product_detail'),
]
