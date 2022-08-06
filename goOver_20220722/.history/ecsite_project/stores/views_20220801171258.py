from django.shortcuts import render
from django.views.generic.list import ListView
from django.contrib.auth.mixins import LoginRequiredMixin

import os
from .models import Products


class ProductListView(LoginRequiredMixin,ListView):
    model = Products
    template_name = os.path.join('stores', 'product_list.html')

    def get_queryset(self):
        query = super().get_queryset()
        product_type_name = self.request.GET.get('product_type_name')
