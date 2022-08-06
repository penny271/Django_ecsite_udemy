from datetime import datetime
from django.shortcuts import render, redirect,  
from django.views.generic.base import (
    View, TemplateView, RedirectView
)


class IndexView(View):

    def get(self, request, *args, **kwargs):
        return render(request, 'index.html')