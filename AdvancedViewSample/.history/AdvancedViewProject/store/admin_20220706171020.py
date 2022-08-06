from django.contrib import admin
from .models import Items

# Register your models here.
#- admin画面でItemsテーブルを利用できるようにする
admin.site.register(Items)