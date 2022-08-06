from tkinter.tix import Tree
from django.db import models
from django.utils import timezone
import pytz

# Create your models here.

class BaseMeta(models.Model):
    # create_at = models.DateTimeField(default=timezone.datetime.now)
    # update_at = models.DateTimeField(default=timezone.datetime.now)
    #- model更新時にwarningが出ることがあり、下記でtimezone関連データ登録時のwarningを消せる
    create_at = models.DateTimeField(default=timezone.datetime.now(pytz.timezone('Asia/Tokyo')))
    update_at = models.DateTimeField(default=timezone.datetime.now(pytz.timezone('Asia/Tokyo')))

    #- abstract = True のものは抽象クラスなのでテーブルとして作成されない
    #- => BaseMetaはテーブルとしてはつくられない
    class Meta:
        abstract = True

#- models.Modelを継承する
# class Person(models.Model):
#- BaseMetaを継承する
class Person(BaseMeta):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    birthday = models.DateField(default='1900-01-01')
    email = models.EmailField(db_index=True)
    salary = models.FloatField(null=True) #- デフォルトはFalse Trueでnullの値を入れることができる
    memo = models.TextField()
    web_site = models.URLField(null=True, blank = True) #- None, '' を入れることができる
    #! BaseMeta で継承したため不要
    # crate_at = models.DateTimeField(default = timezone.datetime.now) #- 作成日時

    class Meta:
        db_table = 'person'
        index_together = [['first_name', 'last_name']]
        #- salary列を昇順にして並び替えしている
        ordering = ['salary']
        #- salary列を降順にして並び替えしている
        # ordering = ['-salary']

    #- main.py の中の print(obj)のobjの名前を変えることができる
    #* Person object (8) => Saburo Ito
    def __str__(self):
        return f'{self.first_name} {self.last_name}'

#- 外部キー
class Students(models.Model):

    name = models.CharField(max_length=20)
    age = models.IntegerField()
    major = models.CharField(max_length=20)
    school = models.ForeignKey(
        # 'Schools', on_delete=models.CASCADE
        # raise ProtectedError を起こすことができる
        'Schools', on_delete=models.RESTRICT
    )
    prefecture = models.ForeignKey(
        'Prefectures', on_delete=models.RESTRICT
    )

    class Meta:
        db_table = 'students'

class Schools(models.Model):

    name = models.CharField(max_length=20)
    prefecture = models.ForeignKey(
        # 'Prefectures', on_delete=models.CASCADE
        'Prefectures', on_delete=models.CASCADE
    )

    class Meta:
        db_table = 'schools'

class Prefectures(models.Model):
    name = models.CharField(max_length=20)

    class Meta:
        db_table = 'prefectures'
