import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ModelExam.settings')
from django import setup
setup()

from ModelApp.models import Students, Test_results, Tests, Classes
from random import randint

#- リスト内表記
class_names = ['Class' + c for c in 'ABCDEFGHIJ']
# print(class_names)







student_names = ['Student' + s in ]
