import os

#- djangoを使ったプロジェクトを読み込むための記述
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ModelProject.settings')
#- ModuleNotFoundError: No module named 'django'
#! vscode のインテープレターの問題なので、djangoが使える環境を選択する
#! ※ Terminalが djangoが入っている仮想環境であっても上記を揃える必要あり!
from django import setup
setup()

from ModelApp.models import Places,Restaurants

places = [Places
    ('Motomachi', 'Yokohama'), ('Tsukiji', 'Tokyo')
]
Restaurants = ['restaurant A', 'restaurant B']

for place_name, place_address in places:
    p = Places(name=place_name, address=place_address )
    p.save()
    for restaurant_name in restaurants:
        r = Restaurants(place=p, name=restaurant_name)
        r.save()


