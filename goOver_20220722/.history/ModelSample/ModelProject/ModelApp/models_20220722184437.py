from tkinter.tix import Tree
from django.db import models
from django.utils import timezone
import pytz

# Create your models here.
class Person(models.Model):
    first_name = models.CharField(m)