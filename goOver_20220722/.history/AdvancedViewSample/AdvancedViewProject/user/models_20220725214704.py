from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    #- Userをimpotし、1対1の外部キーとして使用している
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    website = models.URLField(blank=True)
    picture = models.FileField(upload_to='user/', blank=True)

    def __str__(self):
        #- usernameをつけることで管理画面から観た際に見やすくなる
        #- .usernameで管理画面上で
        return self.user.username