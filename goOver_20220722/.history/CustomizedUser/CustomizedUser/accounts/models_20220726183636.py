# from django.db import models
# from django.contrib.auth.models import (
#     BaseUserManager,AbstractBaseUser,PermissionsMixin
# )

from django.db import models
from django.co


#- オブジェクトに対してマネージャーを設定する必要あり
class UserManager(BaseUserManager):
    #- ユーザーを作成する際のメソッドを定義
    #-普通のユーザー作成時に呼び出される
    def create_user(self, username, email, password = None):
        if not email:
            raise ValueError('Enter Email!')
        #- self.modelでUserクラスが呼び出される
        user = self.model(
            username=username,
            email=email
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, password = None):
        user = self.model(
            username = username,
            email=email,
        )
        user.set_password(password)
        user.is_staff = True
        user.is_active = True
        user.is_superuser = True
        user.save(using=self._db)
        return user

#! password フィールドはすでにAbstractBaseUser に含まれるので、
#! ここで新たにフィールドを設けて、作成する必要なし
#! それ以外で登録したいフィールドを作成する
class User(AbstractBaseUser,PermissionsMixin):
    username = models.CharField(max_length=150)
    email = models.EmailField(max_length=255,unique=True)
    is_active = models.BooleanField(default=False)
    #- 管理画面に入れるユーザかどうかを見分けるフィールド
    is_staff = models.BooleanField(default=False)
    website = models.URLField(null=True)
    picture = models.FileField(null=True)

    #- このユーザーを一意に識別するフィールドを指定
    USERNAME_FIELD = 'email'
    #スーパーユーザ作成時に追加で入力するもの
    REQUIRED_FIELDS = ['username']

    objects = UserManager()

    #- 管理画面上で表示される名前
    def __str__(self):
        return self.email

class Students(models.Model):

    name = models.CharField(max_length=20)
    age = models.IntegerField()
    score = models.IntegerField()
    school = models.ForeignKey(
        'Schools', on_delete=models.CASCADE
    )

    class Meta:
        db_table = 'students'
        verbose_name_plural = '生徒'
        ordering = ('age', )

    def __str__(self):
        return self.name + ': ' + str(self.age)

class Schools(models.Model):
    name = models.CharField(max_length=20, verbose_name='学校名')

    class Meta:
        db_table = 'schools'
        verbose_name_plural = '学校'

    def __str__(self):
        return self.name