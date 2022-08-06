from tkinter.tix import Tree
from django.db import models
from django.utils import timezone
import pytz

# Create your models here.
class Person(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    birthday = models.DateField(default='1900-01-01')
    email = models.EmailField( db_index=True ) # 処理の高速化 データの容量が大きくなる
    salary = models.FloatField(null = True)
    memo = models.TextField(
