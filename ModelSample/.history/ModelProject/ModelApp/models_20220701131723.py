from tkinter.tix import Tree
from django.db import models

# Create your models here.

#- models.Modelを継承する
class Person(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    birthday = models.DateField(default='1900-01-01')
    email = models.EmailField(db_index=True)
    salary = models.FloatField(null=True) #- デフォルトはFalse Trueでnullの値を入れることができる
    memo = models.TextField()
    web_site = models.URLField(null=True, blacnk = true)