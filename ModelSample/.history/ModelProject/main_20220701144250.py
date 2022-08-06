import os

#- djangoを使ったプロジェクトを読み込むための記述
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ModelProject.settings')
#- ModuleNotFoundError: No module named 'django'
#! vscode のインテープレターの問題なので、djangoが使える環境を選択する
#! ※ Terminalが djangoが入っている仮想環境であっても上記を揃える必要あり!
from django import setup
setup()

from ModelApp.models import Person

#- インスタンス化
p = Person(
    first_name = 'Taro', last_name = 'Sato',
    birthday = '2000-01-01', email = 'aa@mail.com',
    salary = 10000, memo= 'memo taro', web_site='http://www.com'
)
p = Person(
    first_name = 'Taro', last_name = 'Sato',
    birthday = '2000-01-01', email = 'aa@mail.com',
    salary = None, memo= 'memo taro', web_site='http://www.com'
)
p = Person(
    first_name = 'Taro', last_name = 'Sato',
    birthday = '2000-01-01', email = 'aa@mail.com',
    salary = None, memo= 'memo taro', web_site=''
)

# p.save()

# classmethod create
Person.objects.create(
    first_name='Jiro', last_name='Ito',
    email = 'bb@mail.com',
    salary = 20000, memo='class method 実行', web_site = None
)

# get_or_create ()
