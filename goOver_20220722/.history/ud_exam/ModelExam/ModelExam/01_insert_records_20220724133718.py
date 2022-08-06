#- ★順番どおりにimportしていかないと以下のようなエラーが出る
#! django.core.exceptions.ImproperlyConfigured: Requested setting INSTALLED_APPS, but settings are not configured. You must either define the environment variable DJANGO_SETTINGS_MODULE or call settings.configure() before accessing settings.
#- setup()してからモデルを呼び出す!
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ModelExam.settings')
from django import setup
setup()

from ModelApp.models import Students, TestsResults, Tests, Classes
from random import randint

class_names = ['Class' + c for c in 'ABCDEFGHIJ']
student_names = ['student' + s for s in 'ABCDEFGHIJ']
test_names = ['数学','英語','国語']

inserted_texts = []
for test_name in test_names:
    test = Tests(
        name = test_name,
    )
    test.save()
    #- 作成したインスタンスを追加する
    


# for class_name in ref_list:
#     class_info = Classes(
#         name = class_name
#     )
#     class_info.save()
#     for student_name in ref_list:
#         student = Students(
#             class_id = class_info,
#             name = student_name,
#             grade = 1,
#         )
#         student.save()
#         for subject in subjects:
#             test = Tests(
#                 name = subject,
#             )
#             test.save()
#             for test_result_info in subjects:
#                 test_result = Tests_results(
#                     student = student,
#                     test = test,
#                     score = randint(50,100),
#                 )
#                 test_result.save()









