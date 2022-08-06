from django.db import models
from django.forms import CharField

# Create your models here.
class Classes(models.Model):
    name = name = models.CharField(max_length=50)

    class Meta:
        db_table = 