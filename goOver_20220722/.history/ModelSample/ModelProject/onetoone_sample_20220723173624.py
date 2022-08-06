import os

#- djangoを使ったプロジェクトを読み込むための記述
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ModelProject.settings')
#- ModuleNotFoundError: No module named 'django'
#! vscode のインテープレターの問題なので、djangoが使える環境を選択する
#! ※ Terminalが djangoが入っている仮想環境であっても上記を揃える必要あり!
from django import setup
setup()

from ModelApp.models import Places,Restaurants

places = [
    ('Motomachi', 'Yokohama'), ('Tsukiji', 'Tokyo')
]
restaurants = ['restaurant A', 'restaurant B','restaurant B','restaurant B','restaurant B',]

for place_name, place_address in places:
    p = Places(name=place_name, address=place_address )
    p.save()
    for restaurant_name in restaurants:
        #- インスタンスで登録、更新する( r.save() )場合は主キーがある場合は常に新しい値で全体を通じて更新されてしまう レクチャー115の更新で説明されている
        #* place=p <= 外部キー兼主キー(models.pyより)
        r = Restaurants(place=p, name=restaurant_name)
        r.save()

        #! django.db.utils.IntegrityError: UNIQUE constraint failed: restaurants.place_id
        #- エラーが発生する - 更新ではなく、insertとなるので、主キーが
        #- 重複することになるため - しかし、restaurantsテーブルに値が
        #- 登録された なぜ??
        # Restaurants.objects.create(
        #     place=p, name=restaurant_name
        # )


