from django.shortcuts import render
from django.views.generic.list import ListView
from django.contrib.auth.mixins import LoginRequiredMixin

import os


class ProductListView(ListView):
    model = Product
    template_name = "TEMPLATE_NAME"

