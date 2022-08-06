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

    item = Items.objects.filter(pk=id).first()
    item = Items.objects.get(id=id)
    return render(request, 'store/item_detail.html', context={
        ''
    })
