import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ModelExam.settings')
from django import setup
setup()

from ModelApp.models import Students, Test_results, Tests, Classes
from random import randint

#- リスト内表記
class_names = ['Class' + c for c in 'ABCDEFGHIJ']
# print(class_names)
student_names = ['Student' + c for c in 'ABCDEFGHIJ']
test_names = ['数学','英語','国語']

inserted_tests = []
#- Testデータベースにtestフィールドを追加している
for test_name in test_names:
    #* インスタンスを作成している
    test = Tests(
        name=test_name
    )
    test.save()
    inserted_tests.append(test)

for class_name in class_names:
    name = Classes(

    )