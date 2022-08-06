from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser, PermissionsMixin,
)
from django.db.models.signals import post_save
from django.dispatch import receiver
from uuid import uuid4 #- uuid作成用
from datetime import datetime, timedelta #- expired_at用
#- (ログイン、ログアウト、メッセージ)
# from django.contrib.auth.models import UserManager

# Create your models here.

class Users(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=255)
    age = models.PositiveIntegerField()
    email = models.EmailField(max_length=255, unique=True)
    is_active = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    picture = models.FileField(null=True, upload_to='picture/')

    #- ログインを実行するには、カスタマイズしたUserにdjango.contrib.auth.models.UserManager か、UserManagerを継承したクラスを指定したobjectsを定義する必要がある
    # objects = UserManager()

    #- このクラスのレコードを一意に定義するのがemail
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    class Meta:
        db_table = 'users'

# #- テーブルのデータ挿入、取り出しをするクラスは、models.Managerを継承して作成する。
class UserActivateTokensManager(models.Manager):

    def activate_user_by_token(self,token):
        user_activate_token = self.filter(
            token=token,
            expired_at__gte=datetime.now()
        ).first()
        #- foreignKeyを利用してuser情報を取得
        user = user_activate_token.user
        user.is_active = True
        user.save()


# class UserActivateTokensManager(models.Manager):

#     def activate_user_by_token(self,token):
#         user_activate_token = self.filter(
#             token=token,
#             expired_at__gte=datetime.now()
#         ).first()
#         #- foreignKeyを利用して、user情報を取得
#         user = user_activate_token.user
#         user.is_active = True
#         user.save()

#- メールでユーザー登録の本登録を完了させるような処理 is_active=Trueにする
class UserActivateTokens(models.Model):

    token = models.UUIDField(db_index=True)
    #-日付型、タイムスタンプ型のカラムが作成される
    expired_at = models.DateTimeField()
    #- foreignKey
    user = models.ForeignKey(
        'Users', on_delete=models.CASCADE
    )

    #- class UserActivateTokenManager(models.Manager):を
    #- views.pyの def activate_user(request, token):で使用するために必要
    # objects = UserActivateTokensManager()

    # class Meta:
    #     db_table = 'user_activate_tokens'

# #- シグナル - 第二引数のsenderで指定したクラス(この場合User)で新たにオブジェクト、レコードがデータベースに追加されるたびに、指定した関数(第一引数)を自動で呼び出す。

@receiver(post_save, sender=Users)
def publish_token(sender,instance, **kwargs):
    #     print(str(uuid4()))
#     print(datetime.now() + timedelta(days=1))
    user_acttivate_token = UserActivateTokens.objects.create(
        #- instanceはsender=Usersに設定されたレコードのインスタンスを取得する
        user = instance, token=str(uuid4()), expired_at=,

    )



# @receiver(post_save, sender=Users)
# def publish_token(sender, instance, **kwargs):
#     print(str(uuid4()))
#     print(datetime.now() + timedelta(days=1))
#     user_activate_token = UserActivateTokens.objects.create(
#         #- 作成したレコード(sender=Users)、この場合USerのインスタンスが第二引数に入る
#         user=instance, token=str(uuid4()), expired_at=datetime.now() + timedelta(days=1),
#     )
#     #- メールでURLを送るほうが良い
#     print(f'http://127.0.0.1:8000/accounts/activate_user/{user_activate_token.token}')