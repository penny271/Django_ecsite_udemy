from datetime import datetime
from django.shortcuts import render, redirect,  get_object_or_404
#- Class Based View(View)最も基本的なView (TemplateView) ホーム画面など、シンプルなテンプレート画面を作成する際に用いる / #- Class Based View(RedirectView) # 別のView, 別のページにリダイレクトをしたい場合に用いられる
from django.views.generic.base import (
    View, TemplateView, RedirectView
)
# #- Class Based View(DetailView) 挿入したデータの詳細を表示
# from django.views.generic.detail import DetailView
# #- Class Based View(ListView) 挿入したデータの一覧を表示したい場合に用いる。
# from django.views.generic.list import ListView
# #- Class Based View(CreateView) 作成したテーブルにデータを挿入したい場合に用いる。/ Class Based View(UpdateView) 挿入したデータを更新したい場合に用いる。/ Class Based View(DeleteView) 挿入したデータを削除したい場合に用いる。 / Class Based View(FormView) 一般にFormを用いる場合使う。
# from django.views.generic.edit import (
#     CreateView,UpdateView, DeleteView, FormView
# )
# from . import forms
# from datetime import datetime
# from .models import Books, Pictures
# #- django.urls.reverse_lazy # 関数名から、その関数を呼び出すパスを返す(success_url, get_absolute_urlに用いる)
# from django.urls import reverse_lazy
# #- データ更新時、削除時などにメッセージを表示するには、SuccessMessageMixinを用いると良い (django.contrib.messages.views.SuccessMessageMixin)
# from django.contrib.messages.views import SuccessMessageMixin
# from django.contrib import messages
# #- logging lec247
# import logging
# from django.http import Http404

# #- settings.pyに記述したloggersの名前で使用できるようになる
# application_logger = logging.getLogger('application-logger')
# error_logger = logging.getLogger('error-logger')

class IndexView(View):

    def get(self, request, *args, **kwargs):

        def get(dhsr)