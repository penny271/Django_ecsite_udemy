from django.contrib import admin
from .models import (
    ProductType, Manufacturers, Products, ProductPictures,
)

# Register your models here.
admin.site.register(
    [ProductType, Manufacturers, Products, ProductPictures,]
)
