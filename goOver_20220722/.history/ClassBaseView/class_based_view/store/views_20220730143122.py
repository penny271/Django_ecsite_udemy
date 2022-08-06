from datetime import datetime
from django.shortcuts import render, redirect,  get_object_or_404
#- Class Based View(View)最も基本的なView (TemplateView) ホーム画面など、シンプルなテンプレート画面を作成する際に用いる / #- Class Based View(RedirectView) # 別のView, 別のページにリダイレクトをしたい場合に用いられる
from django.views.generic.base import (
    View, TemplateView, RedirectView
)


class IndexView(View):

    def get(self, request, *args, **kwargs):
        return render(request, 'index.html')