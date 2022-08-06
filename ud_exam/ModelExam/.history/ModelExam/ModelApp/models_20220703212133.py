from django.db import models

# Create your models here.

# - ForeignKeyがないものから記載していく!!


class Classes(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        db_table = 'classes'


class Students(models.Model):
    name = models.CharField(max_length=50)
    grade = models.IntegerField()
    class_fk = models.ForeignKey('Classes', on_delete=models.CASCADE)

    class Meta:
        db_table = 'students'


class Tests(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        db_table = 'tests'


class Test_results(models.Model):
    score = models.IntegerField()
    students = models.ForeignKey('Students', on_delete=models.CASCADE)
    tests = models.ForeignKey('Tests', on_delete=models.CASCADE)

    class Meta:
        db_table = 'test_results'
