from django.urls import path
from .views import (
    ProductListView, Product_DetailView, add_product,
    CartItemsView,
)

app_name='stores'

urlpatterns = [
    path('product_list', ProductListView.as_view(), name='product_list'),
    path('product_detail/<int:pk>', Product_DetailView.as_view(), name='product_detail'),
    path('add_product/', add_product, name='add_product'),
    path('add_product/', CartItemsView.as_veiw(), name='add_product'),
]
