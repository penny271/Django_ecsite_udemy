from django.shortcuts import render, redirect, get_object_or_404, get_list_or_404
from .models import Items
from django.http import Http404
# Create your views here.

def item_list(request):
    items = Items.objects.all()
    #- 
    items = get_list_or_404(Items, pk__gt=2)
    return render(request, 'store/item_list.html', context={
        'items':items,
    })

def item_detail(request, id):
    #- 強制的に404エラーを起こす
    if id == 0:
        raise Http404
    #- 絞り込んだ後にfirst()が必要 - filter()だとエラーにならない
    # item = Items.objects.filter(pk=id).first()
    #! item = get_list_or_404(Items, pk=id)  <= 間違えて get_list~を記載していた
    #- 指定したモデルを呼び出し、getを行う。値を取得できなかった場合、raise Http404を送出する
    # item = get_object_or_404(Items,name='りんご', pk=id)
    item = get_object_or_404(Items, pk=id)
    #- 存在しないidが当てられたときのための対応 - 一覧にリダイレクトする
    #! is <= オブジェクトを生成すると他のオブジェクトとは重複する事のない一意の番号を保持します。これはid関数で取得することができます。is演算子はこれを比較し、同じオブジェクトであるか（同一）を判断します。
    if item is None:
        return redirect('store:item_list')
    print(item)
    # print(item.name,item.price)
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
    #! htmlの名前は自由に決めてよいがそれ以外は指定の物を使う
    # return render(request, 'store/999.html', status=404)
    #- 強制的に飛ばす
    # return redirect('store:item_list')

#- 500エラー サーバーエラー
def server_error(request):
    return render(request, 'store/500.html', status=500)