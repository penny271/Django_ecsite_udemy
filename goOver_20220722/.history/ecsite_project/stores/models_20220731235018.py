from django.db import models

# Create your models here.

class ProductType(models.Model):
    name = models.CharField(max_length=1000)

    product_type = models.ForeignKey(
        ProductType, on_delete=models.CASCADE
    )

    class Meta:
        db_table = 'product_types'

    def __str__(self):
        return self.name

class Manufacturers(models.Model):
    name = models.CharField(max_length=1000)

    class Meta:
        db_table = 'manufacturers'

    def __str__(self):
        return self.name

class ProductsManager(models.Manager):

    def reduce_stock(self,cart):
        for item in cart.cartitems_set.all():
            update_stock = item.product.stock - item.quantity
            item.product.stock = update_stock
            item.product.save()

class Products(models.Model):
    name = models.CharField(max_length=1000)
    price = models.IntegerField()
    stock = models.IntegerField()
    product_type = models.ForeignKey(ProductType,  on_delete=models.CASCADE)
    manufacturer = models.ForeignKey(
        Manufacturers,  on_delete=models.CASCADE
    )

    objects = ProductsManager()

    class Meta:
        db_table = 'products'

    def __str__(self):
        return self.name


class ProductPictures(models.Model):
    picture = models.FileField(upload_to='product_pictures/')
    product = models.ForeignKey(
        Products, on_delete=models.CASCADE
    )
    order = models.IntegerField()

    class Meta:
        db_table = 'product_pictures'
        ordering = ['order']  # -並び替えのパラメータ

    def __str__(self):
        # return self.name
        # - pictureには名前がないため、self.product.nameから
        #- とってきている
        return self.product.name + ': ' + str(self.order)