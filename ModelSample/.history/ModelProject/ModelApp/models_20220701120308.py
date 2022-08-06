from django.db import models

# Create your models here.

#- models.Modelを継承する
class Person(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)

class Sales(models.Model):
    fee = models.