#- ★順番どおりにimportしていかないと以下のようなエラーが出る
#! django.core.exceptions.ImproperlyConfigured: Requested setting INSTALLED_APPS, but settings are not configured. You must either define the environment variable DJANGO_SETTINGS_MODULE or call settings.configure() before accessing settings.
#- setup()してからモデルを呼び出す!
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ModelExam.settings')
from django import setup
setup()

from ModelApp.models import Students

student = Students.objects.get(pk=1)
for test_result in student.testresults_set.all():
    print(student.class_fk.name, student.name, test_result.test.name,test_result.score )

from django.db.models import Sum, Avg, Max, Min

# GROUP BY クラス名、テスト名
for class_summary in Classes.objects