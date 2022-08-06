from django.http import Http404
from django.shortcuts import render, redirect
from .models import Items
from django.http import Http404
# Create your views here.

def item_list(request):
    items = Items.objects.all()
    return render(request, 'store/itemlist.html', context={
        'items':items,
    })

def item_detail(request, id):
    #- 強制的に404エラーを起こす
    if id == 0:
        raise Http404
    #- 絞り込んだ後にfirst()が必要 - filter()だとエラーにならない
    item = Items.objects.filter(pk=id).first()
    #- 存在しないidが当てられたときのための対応 - 一覧にリダイレクトする
    #! is <= オブジェクトを生成すると他のオブジェクトとは重複する事のない一意の番号を保持します。これはid関数で取得することができます。is演算子はこれを比較し、同じオブジェクトであるか（同一）を判断します。
    if item is None:
        return redirect('store:item_list')
    return render(request,'store/item_detail.html', context={'item':item})

#- リダイレクト import必要
def to_google(request):
    return redirect('https://www.google.com')

#- リダイレクト 内部移動も可能
def one_item(request):
    # item_detail関数を呼び出し、引数id に1を入れる
    return redirect('store:item_detail', id=33)

#- エラーハンドリング 404エラー ページが見つからない場合
def page_not_found(request, exception):
    return render(request, 'store/404.html', status=404)
    #- 強制的に飛ばす
    # return redirect('store:item_list')

def server_error(request):
    return render(request, 'store/500.html', status)