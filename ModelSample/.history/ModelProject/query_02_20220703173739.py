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

from ModelApp.models import Students, Person

# 全件取得 all()
# print(Students.objects.all())

# IN
ids = [13,14,15]
# print(Students.objects.filter(pk__in=ids))

# contain 部分一致
# like '%〇〇%'  SQL 処理事件がかかる すべてのデータを確認するため
# print(Students.objects.filter(name__contains='郎'))

#- nullのもの
# is null
# p = Person(
#     first_name = 'Jiro', last_name='Yamada',
#     birthday = '2000-01-01', email='aa@mail.com',
#     salary = None, memo='memo Jiro', web_site= 'http://sample.com',
# )
# p.save()

#- filter: 指定した条件、 exclude: 指定した条件以外
# print(Person.objects.filter(salary__isnull=True))
# print(Person.objects.exclude(salary__isnull=True))

# print(Students.objects.exclude(name='太郎'))

# values: 一部の列、カラムのみ取得する - 速く処理できる
# print(Students.objects.values('name', 'age').filter(pk=14).query)

students = Students.objects.values('id','name','age')
for student in students:
    print(student['id'])

# 並び替え(order_by)
print(Students.objects.order_by)