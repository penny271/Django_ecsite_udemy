from django.shortcuts import render, redirect
from .models import Items
# Create your views here.

def item_list(request):
    items = Items.objects.all()
    return render(request, 'store/item_list.html', context={
        'items':items,
    })

def item_detail(request, id):
    #- 絞り込んだ後にfirst()が必要 - filter()だとエラーにならない
    item = Items.objects.filter(pk=id).first()
    #- 存在しないidが当てられたときのための対応 - 一覧にリダイレクトする
    #! is <= オブジェクトを生成すると他のオブジェクトとは重複する事のない一意の番号を保持します。これはid関数で取得することができます。is演算子はこれを比較し、同じオブジェクトであるか（同一）を判断します。
    if item is None:
        return redirect('store:item_list')
    return render(request,'store/item_detail.html', context={'item':item})

#- リダイレクト import必要
def to_google(request):
    # return redirect('https://www.google.com')
    return redirect('https://www.google.com')

#- リダイレクト 内部移動も可能
def one_item(request):
    # item_detail関数を呼び出し、引数id に1を入れる
    return redirect('store:item_detail', id=33)