from django.shortcuts import render, redirect, get_object_or_404, get_list_or_404
from .models import Items
from django.http import Http404
# Create your views here.

def item_list(request):
    items = Items.objects.all()
    #- 複数対象 指定したモデルを呼び出し、filterを行う。値を取得できなかった場合、raise Http404を送出する
    # items = get_list_or_404(Items, pk__gt=4)
    return render(request, 'store/item_list.html', context={
        'items':items,
    })

def item_detail(request, id):

    # item = Items.objects.get(id=id)
    item = Items.objects.filter(pk=id).first()
    if item is None:
        return redirect('store:item_list')
    return render(request, 'store/item_detail.html', context={
        'item': item
    })

#- リダイレクト import必要
def to_google(request):
    return redirect('https://www.google.com')

# #- リダイレクト 内部移動も可能
# def one_item(request):
#     # item_detail関数を呼び出し、引数id に1を入れる
#     return redirect('store:item_detail', id=33)

def one_item(request):
    return redirect('store:item_detail', id=1)

# #- エラーハンドリング 404エラー ページが見つからない場合
def page_not_found(request, exception):
    #- status=404 を設定しないとターミナルの結果が 200 となってしまう
    return render(request, 'store/404.html', status=404)
    #! htmlの名前は自由に決めてよいがそれ以外は指定の物を使う
    # return render(request, 'store/999.html', status=404)
    #- 強制的に飛ばす
    return redirect('store:item_list')

# #- 500エラー サーバーエラー
# def server_error(request):
#     return render(request, 'store/500.html', status=500)