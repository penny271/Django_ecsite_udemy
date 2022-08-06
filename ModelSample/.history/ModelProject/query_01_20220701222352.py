# select_foreign_table.py

import os

#- djangoを使ったプロジェクトを読み込むための記述
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ModelProject.settings')
#- ModuleNotFoundError: No module named 'django'
#! vscode のインテープレターの問題なので、djangoが使える環境を選択する
#! ※ Terminalが djangoが入っている仮想環境であっても上記を揃える必要あり!
from django import setup
setup()

from ModelApp.models import Students

# 全件取得
print(Students.objects.all())

# 頭5件取得
# print(Students.objects.all()[:5])

# 5件目より後
# print(Students.objects.all()[5:])

# 6~8件目
# print(Students.objects.all()[5:8])
# print(Students.objects.all()[5:8].query)

# 1番最初の1件
# print(Students.objects.first())

# 同じものみんな
# print(Students.objects.filter(name='太郎'))
# print(Students.objects.filter(age=17))

# AND条件
# print(Students.objects.filter(name='太郎',pk__gt=13).query)
# print(Students.objects.filter(name='太郎',pk__lt=20).query)

# 前方一致、後方一致
print(Students.objects.all())
print(Students.objects.filter(name__startswith='太'))
print(Students.objects.filter(name__startswith='太'))
