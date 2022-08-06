#- ★順番どおりにimportしていかないと以下のようなエラーが出る
#! django.core.exceptions.ImproperlyConfigured: Requested setting INSTALLED_APPS, but settings are not configured. You must either define the environment variable DJANGO_SETTINGS_MODULE or call settings.configure() before accessing settings.
#- setup()してからモデルを呼び出す!
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ModelExam.settings')
from django import setup
setup()

from ModelApp.models import Students, Classes

student = Students.objects.get(pk=1)

#テストスコア表示
#- test_resultはインスタンス全体であるため、要素を取り出すのに、特定のキーで取り出す必要あり
# for test_result in student.testresults.score_set.all(): #! NG!
for test_result in student.testresults_set.all():
    print(student.name, student.class_fk.name, test_result.test.name ,test_result.score)

from django.db.models import Sum, Avg, Max, Min

# GROUP BY クラス名、テスト名
for class_summary in Classes.objects.values('name','students__testresults__test__name').annotate(
    max_score=Max('students__testresults__score'),
    min_score=Max('students__testresults__score'),
    avg_score=Max('students__testresults__score'),
    sum_score=Max('students__testresults__score'),
):
    print(
        class_summary['name'],
        class_summary['students__testresults__test__name'],
        class_summary['max_score'],
        class_summary['min_score'],
        class_summary['avg_score'],
        class_summary['sum_score'],
    )

for class_summary in Classes.objects.values('name','students__testresults__test__name').annotate(
    max_score=Max('students__testresults__score'),
    min_score=Max('students__testresults__score'),
    avg_score=Max('students__testresults__score'),
    sum_score=Max('students__testresults__score'),
):
    print(
        class_summary['name'],
        class_summary['students__testresults__test__name'],
        class_summary['max_score'],
        class_summary['min_score'],
        class_summary['avg_score'],
        class_summary['sum_score'],
    )