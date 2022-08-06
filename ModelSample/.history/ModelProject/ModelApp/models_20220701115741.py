from django.db import models

# Create your models here.

#- models.Modelを継承する
class Person(models.Model):
    first_name = models.CharField(max_length=30)
