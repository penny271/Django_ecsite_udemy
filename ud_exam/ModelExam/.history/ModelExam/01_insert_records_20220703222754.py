# from random import randint
# from ModelApp.models import Students, Test_results, Tests, Classes
# from django import setup
# import os

import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ModelExam.settings')


from random import randint
from ModelApp.models import Students, Test_results, Tests, Classes
from django import setup

# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ModelExam.settings')
# setup()

setup()


#- リスト内表記
class_names = ['Class' + c for c in 'ABCDEFGHIJ']
# print(class_names)
student_names = ['Student' + c for c in 'ABCDEFGHIJ']
test_names = ['数学', '英語', '国語']

#- 以下の過程を言語化すると...
#- Testsインスタンスを3つ作成 => Classesインスタンスを10個作成
#- => 各Classesインスタンスに対してStudentsインスタンスを10個作成
#- => 各Studentsインスタンスに対してTest_resultsインスタンスを10個作成

inserted_tests = []
#- Testデータベースにtestフィールドを追加している
for test_name in test_names:
    # * インスタンスを作成している
    test = Tests(
        name=test_name
    )
    test.save()
    # Test_resultsのオブジェクトを作成するために作成
    inserted_tests.append(test)

#- for文の中にfor文を入れることですべてのパターンを記載している
for class_name in class_names:
    insert_class = Classes(
        name=class_name
    )
    insert_class.save()
    for student_name in student_names:
        #* 単純に名前をわかりやすくするため以下のように記述しているだけ
        name = class_name + ' ' + student_name
        student = Students(
            name=name,
            class_fk=insert_class,
            grade=1,
        )
        student.save()
        for inserted_test in inserted_tests:
            test_result=Test_results(
                student=student,
                test = inserted_test,
                score = randint(50,100), # 50~100の間のランダムな整数
            )
            test_result.save()
