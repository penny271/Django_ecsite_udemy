import os

#- djangoを使ったプロジェクトを読み込むための記述
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ModelProject.settings')
#- ModuleNotFoundError: No module named 'django'
#! vscode のインテープレターの問題なので、djangoが使える環境を選択する
#! ※ Terminalが djangoが入っている仮想環境であっても上記を揃える必要あり!
from django import setup
setup()

from ModelApp.models import Person

#- すべて取得 2. 値を全て取得(allメソッド)
persons = Person.objects.all()
for person in persons:
    print(person.id, person, person.salary)

print('*'*50)

#- 1. getメソッドで絞り込んでデータを取得
person = Person.objects.get(pk=1)
print(person)

print('*'*50)

#- 3. filterで特定の条件で絞り込んで、allで取得
persons = Person.objects.filter(first_name = 'Saburo')
persons2 = Person.objects.filter(first_name = 'Saburo')
print(persons)