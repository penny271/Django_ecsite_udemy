import os

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
p.save()

p = Person(
    first_name = 'Taro', last_name = 'Sato',
    birthday = '1990-04-01', email = 'aa@mail.com',
    salary = 10000, memo= 'memo taro', web_site='http://www.com'
)
p.save()