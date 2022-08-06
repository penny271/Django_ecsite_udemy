from django.db import models

# Create your models here.

class ProductType(models.Model):
    name = models.CharField(max_length=1000)

    class Meta:
        db_table = 'product_types'

    def __str__(self):
        return self.name