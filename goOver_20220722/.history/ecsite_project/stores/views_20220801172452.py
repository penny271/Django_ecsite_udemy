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
        # - 何もない場合は None を取得
        product_type_name = self.request.GET.get('product_type_name', None)
        if product_type_name:
            query = query.filter(
                product_type__name=product_type_name
            )
        return query

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # - 何もない場合は 空白 を取得

        context["product_type_name"] = self.request.GET.get('product_type_name', '')
        return context

