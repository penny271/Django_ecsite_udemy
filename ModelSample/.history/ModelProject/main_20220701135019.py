import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ModelPfoject.settings')
from django import setup
setup()

from ModelApp.models import Person

p = Person(
    first_name = 'Taro', last_name = 'Sato',
    birthday = ''
)
