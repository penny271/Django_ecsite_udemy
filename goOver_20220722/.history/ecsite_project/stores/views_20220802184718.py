from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.
from django.contrib.auth.mixins import LoginRequiredMixin

import os
from .models import Products


class ProductListView(LoginRequiredMixin,ListView):
    model = Products
    template_name = os.path.join('stores', 'product_list.html')

    def get_queryset(self):
        query = super().get_queryset()
        # - 何もない場合は None を取得
        product_type_name = self.request.GET.get('product_type_name', None) # 検索wordを取得
        product_name = self.request.GET.get('product_name', None)
        if product_type_name:
        #- 外部キーによる絞り込み
        #- filter(外部キー名__外部のテーブルのカラム名=絞り込みたい値)
            query = query.filter(
                product_type__name=product_type_name
            )
        if product_name:
            query = query.filter(
                name=product_name
            )
        order_by_price = self.request.GET.get('order_by_price', None)
        # if order_by_price == 1: #- '1' 文字列である必要あり!!
        if order_by_price == '1': #- '1' 文字列である必要あり!!
            query = query.order_by('price')
        elif order_by_price == '2':
            query = query.order_by('-price')
        return query

    #- inputに検索ワード入力、検索後も検索ワードが残る設定
    #- value={}を設定  <p>商品タイプ: <input type="text" name="product_type_name" value="{{product_type_name}}"></p>
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # - 何もない場合は 空白 を取得
        context["product_type_name"] = self.request.GET.get('product_type_name', '')
        context["product_name"] = self.request.GET.get('product_name', '')
        order_by_price = self.request.GET.get('order_by_price', 0)
        if order_by_price == '1':
            context['ascending'] = True
        elif order_by_price == '2':
            context['descending'] = True
        return context


