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