from django.urls import path
from .views import (
    ProductListView, Product_DetailView, add_product,
    CartItemsView,CartUpdateForm,Delete
)

app_name='stores'

urlpatterns = [
    path('product_list', ProductListView.as_view(), name='product_list'),
    path('product_detail/<int:pk>', Product_DetailView.as_view(), name='product_detail'),
    path('add_product/', add_product, name='add_product'),
    path('cart_items/', CartItemsView.as_view(), name='cart_items'),
    path('cart_items/', CartItemsView.as_view(), name='cart_items'),
]
