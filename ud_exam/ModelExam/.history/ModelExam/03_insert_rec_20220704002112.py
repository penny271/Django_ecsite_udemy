#- ★順番どおりにimportしていかないと以下のようなエラーが出る
#! django.core.exceptions.ImproperlyConfigured: Requested setting INSTALLED_APPS, but settings are not configured. You must either define the environment variable DJANGO_SETTINGS_MODULE or call settings.configure() before accessing settings.
#- setup()してからモデルを呼び出す!
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ModelExam.settings')
from django import setup
setup()

from ModelApp.models import Students, TestResults, Tests, Classes
from random import randint


#- リスト内表記
class_names = ['Class' + c for c in 'ABCDEFGHIJ']
# print(class_names)
student_names = ['Student' + c for c in 'ABCDEFGHIJ']
test_names = ['数学', '英語', '国語']

#- 以下の過程を言語化すると...
#- Testsインスタンスを3つ作成 => Classesインスタンスを10個作成
#- => 各Classesインスタンスに対してStudentsインスタンスを10個作成
#- => 各Studentsインスタンスに対してTestResultsインスタンスを10個作成

inserted_tests = []
#- Testデータベースにtestフィールドを追加している
for test_name in test_names:
    test = Tests(
        name = test_name
    )
    test.save()
    inserted_tests.append(test)


for class_name in class_names:
    insert_class = Classes(
        name = class_name
    )
    insert_class.save()
    for student_name in student_names:
        student = Students(
            name = student_name,
            
        )







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
            test_result=TestResults(
                student=student,
                test = inserted_test,
                score = randint(50,100), # 50~100の間のランダムな整数
            )
            test_result.save()

#! sqlite3.OperationalError: table test_results has no column named student_id
#- このようなエラーが出た => 最初に登録したデータベースの情報を書き変えていなかったため起こった!! makemigrations をして治らなければ、データベースを初期化してみる - 20220703
