from django.shortcuts import render
from django.views.generic.list import ListView
from django.contrib.auth.mixins import LoginRequiredMixin

import os
from .models import Products


class ProductListView(LoginRequiredMixin,ListView):
    model = Products
    template_name = os.path.join('stores', 'product_list.html')

    query