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
    author1 = Authors(name='Authors1')
    author2 = Authors(name='Authors2')
    author3 = Authors(name='Authors3')
    author1.save()
    author2.save()
    author3.save()

insert_books()
insert_authors()

# book1 = Books.objects.get(pk=1)
# book3 = Books.objects.get(pk=3)
# author1 = Authors.objects.get(pk=1)
# author2 = Authors.objects.get(pk=2)
# author3 = Authors.objects.get(pk=3)

#- authors.addは books_authorsテーブルに表示させる
#- 主キー名となるもの authors_id 任意に決められる
# book1.authors.add(author1,author2)

#- 多対多 の場合は .all() が必要
# print(book1.authors.all())

# book3.authors.add(author1)
# book3.authors.add(author2,author3)