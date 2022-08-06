# select_foreign_table.py

import os

#- djangoを使ったプロジェクトを読み込むための記述
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ModelProject.settings')
#- ModuleNotFoundError: No module named 'django'
#! vscode のインテープレターの問題なので、djangoが使える環境を選択する
#! ※ Terminalが djangoが入っている仮想環境であっても上記を揃える必要あり!
from django import setup
setup()

from ModelApp.models import Students,Schools,Prefectures

s = Schools.objects.first()
# print(type(s))
#- dir()でインスタンスが持っているメソッドやプロパティを確認できる
# print(dir(s))
# print(s.prefecture.name)
# print(s.students_set.all())

# 1件だけデータを取得できる
# s = Schools.objects.first()
# print(type(s))
# #- 使えるメソッドの一覧が見れる 1対多 の関係等確認できる
# print(dir(s))
# print(s.prefecture.name)
# print(s.students_set)
# st = s.students_set
# print(type(st))
# print(dir(st))
# print(st.all())
# print(s.students_set.all())

from ModelApp.models import Places, Restaurants

# p = Places.objects.first()
# print(type(p))
# print(dir(p))
# print(p.restaurants.name)
# r = Restaurants.objects.first()
# print(r.place.name)

from ModelApp.models import Books, Authors

book = Books.objects.first()
print(dir(book))
b = book.authors.
print(b)

