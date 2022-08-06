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

from ModelApp.models import Students, Schools

for student in Students.objects.all():
    print(student.name, student.school.name, student.school.prefecture)

#- 外部テーブルでフィルター
#^ Model.objects.filter(外部テーブル__カラム=‘○○’) # 外部テーブルのカラムを指定して絞込み
# for student in Students.objects.filter(school__name='南高校'):
#     print(student.name, student.school.name, student.school.prefecture)

for student in Students.objects.filter(school__name='東高校'):
    print(student.name)

#- 外部テーブルでexclude
# for student in Students.objects.exclude(school__name='南高校'):
#     print(student.name, student.school.name, student.school.prefecture)

# print(Students.objects.filter(school__name='東高校').query)

# #- ORDER BY
# for student in Students.objects.order_by('-school__name'):
#     print(student.name, student.school.name, student.school.prefecture)

# #- GROUP BY
# from django.db.models import Count, Max, Sum

# print(Students.objects.values('school__name').annotate(Count('id'),Max('id'), Sum('id')))