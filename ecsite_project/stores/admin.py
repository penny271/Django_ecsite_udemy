from django.contrib import admin
from .models import (
    ProductType, Manufacturers, Products, ProductPictures
)

#- アプリケーションのフォルダ内にあるadmin.pyに以下のように管理対象のモデルを追加すると、そのモデル を管理画面上で扱えるようになります。
admin.site.register(
    [ProductType, Manufacturers, Products, ProductPictures]
)