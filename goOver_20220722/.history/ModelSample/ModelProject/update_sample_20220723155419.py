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
from django.utils import timezone
import pytz

person = Person.objects.get(id=1)
print(person)
person.birthday = '2001-01-01'
person.update_at = timezone.datetime.now(pytz.timezone('Asia/Tokyo'))
person.save()

# persons = Person.objects.filter(first_name = 'Taro')
# #! 一回ごとレコードを処理するため遅い - いっぺんに変更したほうが効率が良い
# for person in persons:
#     print(person)
#     person.first_name = person.first_name.lower()
#     person.update_at = timezone.datetime.now(pytz.timezone('Asia/Tokyo'))
#     person.save()

#- 1回の実行ですべての変更を行えるのでfor文を使うよりも処理が断然早い
# Person.objects.filter(first_name='Saburo').update(
#     web_site='http://sample.jp',
#     update_at = timezone.datetime.now(pytz.timezone('Asia/Tokyo'))
#     )

single = Person.objects.get(first_name	='abc')
single.first_name = 'ccc'
single.email = 'single@mail.com'
single.save()
print(single)

Person.objects.filter(last_name = 'Sakamoto').update(
    last_name='Keen'
)
