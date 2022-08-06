import os
#- djangoを使ったプロジェクトを読み込むための記述
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ModelProject.settings')
#- ModuleNotFoundError: No module named 'django'
#! vscode のインテープレターの問題なので、djangoが使える環境を選択する
#! ※ Terminalが djangoが入っている仮想環境であっても上記を揃える必要あり!
from django import setup
setup()

from ModelApp.models import Person

#- 1. 対象のModelのインスタンスを作成してsaveを実行します。

p = Person(
    first_name='Taro', last_name='Sato',
    salary=None, memo='memo taro', web_site=''
)
p.save()

#- 2. クラスのcreateメソッドを用います。
Person.objects.create(
    first_name='Jiro', last_name='Ito',
    email='bb@mail.com',
    salary=20000, memo='class method 実行', web_site=None
)

#- 3. get_or_createメソッドを実行する。
obj, created = Person.objects.get_or_create(
    first_name='Saburo', last_name='Ito',
    email='bb@mail.com',
    salary=20000, memo='class method 実行', web_site=None
)

print(f'{')
print(created)
