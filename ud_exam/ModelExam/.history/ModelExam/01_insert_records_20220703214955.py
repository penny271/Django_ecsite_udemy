from random import randint
from ModelApp.models import Students, Test_results, Tests, Classes
from django import setup
import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ModelExam.settings')
setup()


#- リスト内表記
class_names = ['Class' + c for c in 'ABCDEFGHIJ']
# print(class_names)
student_names = ['Student' + c for c in 'ABCDEFGHIJ']
test_names = ['数学', '英語', '国語']

inserted_tests = []
#- Testデータベースにtestフィールドを追加している
for test_name in test_names:
    # * インスタンスを作成している
    test = Tests(
        name=test_name
    )
    test.save()
    inserted_tests.append(test)

#- for文の中にfor文を入れることですべてのパターンを記載している
for class_name in class_names:
    insert_class = Classes(
        name=class_name
    )
    insert_class.save()
    for student_name in student_names:
        name = class_name + ' ' + student_name
        student = Students(
            name=name,
            class_fk=insert_class,
            grade = 1
        )