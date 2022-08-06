#- ★順番どおりにimportしていかないと以下のようなエラーが出る
#! django.core.exceptions.ImproperlyConfigured: Requested setting INSTALLED_APPS, but settings are not configured. You must either define the environment variable DJANGO_SETTINGS_MODULE or call settings.configure() before accessing settings.
#- setup()してからモデルを呼び出す!
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ModelExam.settings')
from django import setup
setup()

# from ModelApp.models import Students, TestResults, Tests, Classes
# from random import randint

from ModelApp.models import Students, Tests_results, Tests, Classes
from random import randint

ref_list = ['A','B','C','D','E','F','G','H','I','J']

for class_name in ref_list:
    class_info = Classes(
        name = class_name
    )
    class_info.save()
    for student_name in ref_list:
        student = Students(
            class_id = class_info,
            name = student_name
        )
        class_id = class_info




