from django.shortcuts import render
from .models import Items
# Create your views here.

def item_list(request):
    items = Items.
    return render(request, 'store/item_list.html')