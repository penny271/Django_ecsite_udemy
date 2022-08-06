from django.db import models
from django.urls import reverse_lazy
#- signalを使う準備
from django.dispatch import receiver
import os
#- logging
import logging
from django.dispatch import receiver #- シグナル
import os

application_logger = logging.getLogger('application-logger')

# Create your models here.
class BaseModel(models.Model):
    create_at = models.DateTimeField()
    update_at = models.DateTimeField()

    #-This model will then not be used to create any database table. Instead, when it is used as a base class for other models, its fields will be added to those of the child class.
    #- つまりabstract = Trueの持つフィールドをclassを継承することで再利用できる abstract = Trueのクラスのモデルはデータベースに作成されない
    class Meta:
        abstract = True

#-BaseModelを継承することでフィールドを引き継げる
class Books(BaseModel):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=1000)
    price = models.IntegerField()

    class Meta:
        db_table = 'books'

    #- CreateViewやUpdateViewでモデルが更新された際に自動で実行される
    def get_absolute_url(self):
        return reverse_lazy("store:detail_book", kwargs={"pk": self.pk})


#     #- Class Based View(CreateView) (Model)get_absolute_url = ‘’ # こちらは、対象のモデルに定義する
#     #- forms.pyを通じて新たにデータが追加されると自動で以下に遷移する
#     def get_absolute_url(self):
#         return reverse_lazy('store:detail_book', kwargs={'pk':self.pk})

#- 整形したデータを取得する役割
class PicturesManager(models.Manager):
    #- 引数bookはviews.pyのpictures = Pictures.objects.filter_by_book(book=self.object)から来ている
    def filter_by_book(self, book):
        print('book: ',book)
        return self.filter(book=book).all()

class Pictures(BaseModel):

    picture = models.FileField(upload_to='picture/')
    book = models.ForeignKey(
        'books', on_delete=models.CASCADE
    )
    abc = 'abc' #test
    objects = PicturesManager()

# #- Picturesが消されたときに発動
# #! post_delete インスタンスのdelete()実行直後
# @receiver(models.signals.post_delete, sender=Pictures)
# def delete_picture(sender, instance, **kwargs):
#     if instance.picture:
#         if os.path.isfile(instance.picture.path):
#             os.remove(instance.picture.path)
#             application_logger.info(f'{instance.picture.path}を削除しました。')

@receiver(models.signals.post_delete, sender=Pictures)
#- instanceの中に削除されたpictureの情報が入っている views.pyのpicture.delete()
def delte(sender, instance, **kwargs):





