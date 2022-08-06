from django.db import models
from django.forms import CharField

# Create your models here.
class Classes(models.Model):
    name = name = models.CharField(max_length=50)

    class Meta:
        db_table = 'classes'

    def __str__(self):
        return self.name

class Tests(models.Model):
    name = name = models.CharField(max_length=50)

    class Meta:
        db_table = 'tests'

    def __str__(self):
        return self.name

    name = name = models.CharField(max_length=50)

    class Meta:
        db_table = 'classes'

    def __str__(self):
        return self.name