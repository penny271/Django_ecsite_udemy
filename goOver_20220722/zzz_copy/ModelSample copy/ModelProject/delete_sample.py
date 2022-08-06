import os

import pytz

#- djangoを使ったプロジェクトを読み込むための記述
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ModelProject.settings')
#- ModuleNotFoundError: No module named 'django'
#! vscode のインテープレターの問題なので、djangoが使える環境を選択する
#! ※ Terminalが djangoが入っている仮想環境であっても上記を揃える必要あり!
from django import setup
setup()

from ModelApp.models import Person

person = Person.objects.filter(first_name='Saburo').delete()
person = Person.objects.filter(first_name='taro', birthday='2001-01-01').delete()

# 全件削除する
Person.objects.all().delete()