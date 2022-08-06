import os

#- djangoを使ったプロジェクトを読み込むための記述
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ModelProject.settings')
#- ModuleNotFoundError: No module named 'django'
#! vscode のインテープレターの問題なので、djangoが使える環境を選択する
#! ※ Terminalが djangoが入っている仮想環境であっても上記を揃える必要あり!
from django import setup
setup()

from ModelApp.models import Students, Schools, Prefectures

prefectures = ['東京','大阪']
schools = ['東高校','西高校','北高校','南高校',]
students = ['太郎','次郎','三郎']

def insert_records():
    for prefecture_name in prefectures:
        prefecture = Prefectures(
            name=prefecture_name
        )
        prefecture.save()
        for school_name in schools:
            school = Schools(
                name = school_
            )