from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser, PermissionsMixin,
)
# from django.db.models.signals import post_save
# from django.dispatch import receiver
# from uuid import uuid4 #- uuid作成用
# from datetime import datetime, timedelta #- expired_at用
# #- (ログイン、ログアウト、メッセージ)
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