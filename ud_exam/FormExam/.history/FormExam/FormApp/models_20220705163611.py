from msilib.schema import Class
from django.db import models

# Create your models here.
class Students(models.Model):
    age = models.IntegerField()
    name = models.CharField(max_length=50)
    
