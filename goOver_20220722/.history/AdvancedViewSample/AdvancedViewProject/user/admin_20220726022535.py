from django.contrib import admin
#- user.models import Profileは恐らく
from user.models import Profile
# Register your models here.

admin.site.register(Profile)