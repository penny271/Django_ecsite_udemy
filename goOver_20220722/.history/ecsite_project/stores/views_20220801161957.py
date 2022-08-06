from django.shortcuts import render
from django.views.generic.list import ListView
from django.contrib.auth.mixins import LoginRequiredMixin

import os


class MODEL_NAMPEListView(ListView):
    model = P
    template_name = "TEMPLATE_NAME"

