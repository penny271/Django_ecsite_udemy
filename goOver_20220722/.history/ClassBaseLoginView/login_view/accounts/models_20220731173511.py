from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser, PermissionsMixin,
)
from django.urls import reverse_lazy
# Register your models here.


class UserManager(BaseUserManager):
    def create_user(self, username, email, password=None):
        if not email:
            raise ValueError('Enter Email')
        user = self.model(
            username=username,
            email=email,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

class Users(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=150)
    email = models.CharField(max_length=255, unique=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = 'email' #- このテーブルのレコードを一意に識別するフィールド
    REQUIRED_FIELDS = ['username',] #- superuser作成時に必要なフィールド

    objects = UserManager()

    def def get_absolute_url(self):
        from django.core.urlresolvers import reverse
        return reverse('', kwargs={'pk': self.pk})

    def get_absolute_url(self):
        return reverse_lazy('accounts:home')