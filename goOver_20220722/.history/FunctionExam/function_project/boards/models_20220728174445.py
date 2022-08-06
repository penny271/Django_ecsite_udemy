from tkinter import CASCADE
from turtle import ondrag
from django.db import models

# Create your models here.

#- テーブルのデータ挿入、取り出しをするクラスは、models.Managerを継承して作成する。
#- id順で取り出すため、ThemeMaanger(models.Manager)を使用している
class ThemesManager(models.Manager):

    def fetch_all_themes(self):
        return self.order_by('id').all()

class Themes(models.Model):

    title = models.CharField(max_length=255)
    user = models.ForeignKey(
        'accounts.Users', on_delete=models.CASCADE
    )

    #- ThemesManager(models.Manager):を呼び出せるようにobjects作成
    objects = ThemesManager()

    class Meta:
        db_table = 'themes'

class CommentsManager(models.Manager):
    def fetch_by_theme_id(self, theme_id):
        #- 一つのthemeに対してコメントは複数ある
        return self.filter(theme_id=theme_id).order_by('id').all()




class CommentsManage(models.Manager):
    def fetch_

class Comments(models.Model):
    comment = models.CharField(max_length=1000)
    user = models.ForeignKey(
        'accounts.Users', on_delete=models.CASCADE
    )
    theme = models.ForeignKey(
        'Themes', on_delete=models.CASCADE
    )

    objects = CommentsManager()

    class Meta:
        db_table = 'comments'