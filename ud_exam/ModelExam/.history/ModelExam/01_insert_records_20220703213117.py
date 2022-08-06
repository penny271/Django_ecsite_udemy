import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ModelExam.settings')
from django import setup
setup()

from ModelApp.models import Students, Test_results, Tests, Classes
from random import randint

#-
class_names = [for c in 'ABCDEFGHIJ']
