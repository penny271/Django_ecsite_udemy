from django.db import models

# Create your models here.

class Test_results(models.Model):
    score = models.IntegerField()
    tests = models.ForeignKey('tests',delete_on=models.CASCADE)
    students = models.ForeignKey('students', delete_on=models.CASCADE)


class Tests(models.Model):
    name = models.CharField(max_length=50)

class Students(models.Model):
    name = models.CharField(max_length=50)
    grade = models.int


class Classes(models.Model):

