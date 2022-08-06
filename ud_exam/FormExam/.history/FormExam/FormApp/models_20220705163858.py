# from msilib.schema import Class
from django.db import models
from django.forms import FileField

# Create your models here.
class Students(models.Model):
    age = models.IntegerField()
    name = models.CharField(max_length=50)
    grade = models.IntegerField()
    pictures = models.FileField(upload_to='student/')

    class Meta:
        db_table= 'students'
