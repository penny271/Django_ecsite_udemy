from django.db import models

# Create your models here.

class Test_results(models.Model):
    score = models.IntegerField()
    tests = models.ManyToManyField(Tests,delete_on=models.CASCADE)


class Tests()
