from django.db import models

# Create your models here.

class Test_results(models.Model):
    score = models.IntegerField()
    tests = models.ManyToManyField('tests',delete_on=models.CASCADE)


class Tests(models.Model):
    name = models.CharField(max_length=50)
