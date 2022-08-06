# select_foreign_table.py

from distutils.command.build_scripts import first_line_re
import os

#- djangoを使ったプロジェクトを読み込むための記述
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ModelProject.settings')
#- ModuleNotFoundError: No module named 'django'
#! vscode のインテープレターの問題なので、djangoが使える環境を選択する
#! ※ Terminalが djangoが入っている仮想環境であっても上記を揃える必要あり!
from django import setup
setup()

from ModelApp.models import Students

# print(Students.objects.all())

#- 件数
# print(Students.objects.count())
# print(Students.objects.filter(name='太郎').count())

#- # 件数、最大値、最小値、平均値、合計
# from django.db.models import Count, Max, Min, Avg, Sum
# print(Students.objects.aggregate(Count('pk'),Max('pk'), Min('pk'), Avg('pk'), Sum('age')))
# aggregate_student = Students.objects.aggregate(counted_pk=Count('pk'),max_pk = Max('pk'), min_pk = Min('pk'), avg_pk=Avg('pk'), sum_aga=Sum('age'))
# print(aggregate_student)

# print(aggregate_student['pk__avg'])

# GROUP BY: ある特定のカラムで集計して、合計、最大などを求める