import os

#- djangoを使ったプロジェクトを読み込むための記述
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ModelProject.settings')
#- ModuleNotFoundError: No module named 'django'
#! vscode のインテープレターの問題なので、djangoが使える環境を選択する
#! ※ Terminalが djangoが入っている仮想環境であっても上記を揃える必要あり!
from django import setup
setup()

from ModelApp.models import Books, Authors

def insert_books():
    book1 = Books(name='Book1')
    book2 = Books(name='Book2')
    book3 = Books(name='Book3')
    book1.save()
    book2.save()
    book3.save()

def insert_authors():
    book1 = Books(name='Book1')
    book2 = Books(name='Book2')
    book3 = Books(name='Book3')
    book1.save()
    book2.save()
    book3.save()