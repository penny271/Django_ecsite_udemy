import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ModelPfoject.settings')
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