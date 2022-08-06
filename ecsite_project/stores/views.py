from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse, Http404
from django.views.generic.base import TemplateView
from django.views.generic.edit import (
    UpdateView,DeleteView,CreateView
)
from django.urls import reverse_lazy
from .forms import (
    CartUpdateForm, AddressInputForm
)
from django.core.cache import cache
#- データベースの原子性
from django.db import transaction

import os
from .models import(
    Products, Carts, CartItems,Addresses, Orders, OrderItems,
)


class ProductListView(LoginRequiredMixin, ListView):
    model = Products
    # - ここで stores/product_list.html のように
    #- アプリケーションごとの保存場所を指定している
    template_name = os.path.join('stores', 'product_list.html')

    # - def get_queryset(self): # データを取得する際のSQLを定義する。
    def get_queryset(self):
        query = super().get_queryset()
        print(query)
        # - 何もない場合は None を取得
        product_type_name = self.request.GET.get('product_type_name', None)
        product_name = self.request.GET.get('product_name', None)
        if product_type_name:
            query = query.filter(
                #- 外部キーによる絞り込み
                #- filter(外部キー名__外部のテーブルのカラム名=絞り込みたい値)
                product_type__name=product_type_name
            )
        if product_name:
            query = query.filter(
                # - あるテーブルのカラムで絞り込む場合は、filter(カラム名=絞り込みたい値)
                name=product_name
            )
        order_by_price = self.request.GET.get('order_by_price', 0)
        if order_by_price == '1':
            query = query.order_by('price')
        elif order_by_price == '2':
            query = query.order_by('-price')
        return query

    # - def get_context_data(self, **kwargs): # テンプレートに渡す値を指定する
    # - 検索ワードを 実行する ボタンを押した後も引き続き残すための処理
    # <p>商品タイプ: <input type="text" name="product_type_name" value=" {{ product_type_name }}"></p> のvalueの値を設定 = 初期値としての役割を果たす
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # - 何もない場合は '' を取得
        context['product_type_name'] = self.request.GET.get('product_type_name', '')
        context['product_name'] = self.request.GET.get('product_name', '')
        order_by_price = self.request.GET.get('order_by_price')
        if order_by_price == '1':
            context['ascending'] = True
        elif order_by_price == '2':
            context['descending'] = True
        return context


class ProductDetailView(LoginRequiredMixin, DetailView):
    model = Products
    template_name = os.path.join('stores', 'product_detail.html')

    def get_context_data(self, **kwargs):
        print('kwargs: ',kwargs) #kwargs:  {'object': <Products: プレイステーション>}
        context = super().get_context_data(**kwargs)
        context['is_added'] = CartItems.objects.filter(
            cart_id=self.request.user.id,
            product_id=kwargs.get('object').id
        ).first()
        return context

@login_required
def add_product(request):
    # if request.is_ajax:  <=  Django4.0以上では使えない
    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        product_id = request.POST.get('product_id')
        quantity = request.POST.get('quantity')
        # - 指定したモデルを呼び出し、getを行う。値を取得できなかった場合、raise Http404を送出する 例)
        product = get_object_or_404(Products, id=product_id)
        if int(quantity) > product.stock:
            response = JsonResponse({'message':'在庫数が超えています'})
            print('エラー1')
            print('response:', response)
            response.status_code = 403 #html側でerrorとして受け取るため
            return response
        if int(quantity) <= 0:
            response = JsonResponse({'message':'0より大きい値を入力してください'})
            print('response:', response)
            print('エラー2')
            response.status_code = 403
            return response
        #- 結果がタプル型で返ってくる
        cart = Carts.objects.get_or_create(
            user=request.user
        )
        if all([product_id, cart, quantity]):
            #- models.py の CartItemManager(models.Manager)の中の
            #- def save_item()を使用している
            CartItems.objects.save_item(
                quantity=quantity, product_id=product_id,
                #- タブル型なのでcart[0]として取り出している
                cart=cart[0]
            )
            return JsonResponse({'message': '商品をカートに追加しました'})

class CartItemsView(LoginRequiredMixin, TemplateView):
    template_name = os.path.join('stores','cart_items.html')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user_id = self.request.user.id
        query = CartItems.objects.filter(cart_id=user_id)
        total_price = 0
        items = []
        for item in query.all():
            total_price += item.quantity * item.product.price
            #- ProductPicturesのインスタンスを取得している
            picture = item.product.productpictures_set.first()
            #- ProductPicturesのインスタンスのpictureを取得している
            picture = picture.picture if picture else None
            in_stock = True if item.product.stock >= item.quantity else False
            tmp_item = {
                'quantity': item.quantity,
                'picture': picture,
                'name': item.product.name,
                'id': item.id,
                'price': item.product.price,
                'in_stock': in_stock,
            }
            items.append(tmp_item)
        context['total_price'] = total_price
        context['items'] = items
        return context

class CartUpdateView(LoginRequiredMixin, UpdateView):
    template_name = os.path.join('stores', 'update_cart.html')
    # template_name = os.path.join('stores', 'delete_cart.html')
    form_class = CartUpdateForm
    model = CartItems
    success_url = reverse_lazy('stores:cart_items')

class CartDeleteView(LoginRequiredMixin, DeleteView):
    template_name = os.path.join('stores', 'delete_cart.html')
    model = CartItems
    success_url = reverse_lazy('stores:cart_items')

class InputAddressView(LoginRequiredMixin, CreateView):
    template_name = os.path.join('stores','input_address.html')
    form_class = AddressInputForm
    success_url = reverse_lazy('stores:confirm_order')

    #- cartが空の場合、遷移させないようにしている
    #- lec270 住所を選択できるようにするためにurls.pyに引数をpkを追加した
    #- よって、この文の引数がないとエラーになるため、pk=Noneを設定する
    # def get(self, request):
    def get(self, request, pk=None):
        cart = get_object_or_404(Carts, user_id=request.user.id)
        if not cart.cartitems_set.all():
            raise Http404('商品が入っていません')
        return super().get(request, pk)

    #- addressをcacheする
    def get_context_data(self, **kwarg):
        context = super().get_context_data(**kwarg)
        #- keyに該当する値をキャッシュから取り出す。存在しない場合 は、defaultを返す keyは forms.pyの cache.set(f'address_user_{self.user.id}',address)の 'address_user_{self.user.id}'　
        address = cache.get(f'address_user_{self.request.user.id}')
        #- pkの取得方法 lec270 住所を選択できるようにするためにurls.pyに引数をpkを追加したしたため、下記の用にpkを取得できる
        pk = self.kwargs.get('pk')
        address = get_object_or_404(Addresses, user_id=self.request.user.id, pk=pk) if pk else address
        if address:
            print('context-',context) # context- {'form': <AddressInputForm bound=False, valid=Unknown, fields=(zip_code;prefecture;address)>, 'view': <stores.views.InputAddressView object at 0x7fdba1a55520>}
            print('address-',address) # address- 123-3456 兵庫県 CCC Street 274
            #- キャッシュした値を初期値としてフィールドに入力したままにする
            context['form'].fields['zip_code'].initial = address.zip_code
            context['form'].fields['prefecture'].initial = address.prefecture
            context['form'].fields['address'].initial = address.address
        context['addresses'] = Addresses.objects.filter(user=self.request.user).all()
        return context

    #- # formの送信時の処理をカスタマイズする。
    def form_valid(self,form):
        #- def form.valid()の中でform.userに値を与えている
        form.user = self.request.user
        return super().form_valid(form)

class ConfirmOrderView(LoginRequiredMixin, TemplateView):
    template_name=os.path.join('stores','confirm_order.html')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        address = cache.get(f'address_user_{self.request.user.id}')
        context['address'] = address
        cart = get_object_or_404(Carts, user_id=self.request.user.id)
        context['cart'] = cart
        total_price = 0
        items = []
        for item in cart.cartitems_set.all():
            total_price += item.quantity * item.product.price
            picture = item.product.productpictures_set.first()
            picture = picture.picture if picture else None
            tmp_item = {
                'quantity':item.quantity,
                'picture':picture,
                'name':item.product.name,
                'price':item.product.price,
                'id':item.id,
            }
            items.append(tmp_item)
        context['total_price'] = total_price
        context['items'] = items
        return context

    #- データベースの原子性
    @transaction.atomic
    def post(self, request, *args, **kwargs):
        #- def get_context_data()のget_context_data()を呼び出してcontext及び中身 を取り出すことができる
        context = self.get_context_data()
        address = context.get('address')
        cart = context.get('cart')
        total_price = context.get('total_price')
        print(context)
        print('\n', 'all:', address, cart, total_price)
        if (not address) or (not cart) or (not total_price):
            raise Http404('注文処理でエラーが発生しました')
        for item in cart.cartitems_set.all():
            if item.quantity > item.product.stock:
                raise Http404('注文処理でエラーが発生しました')

        order = Orders.objects.insert_cart(cart,address,total_price)
        OrderItems.objects.insert_cart_items(cart, order)
        Products.objects.reduce_stock(cart)
        cart.delete()
        return redirect(reverse_lazy('stores:order_success'))

class OrderSuccessView(LoginRequiredMixin, TemplateView):

    template_name = os.path.join('stores', 'order_success.html')