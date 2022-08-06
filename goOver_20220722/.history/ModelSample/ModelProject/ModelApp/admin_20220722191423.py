from django.contrib import admin
from .models import Person

# Register your models here.
#- 拡張機能のおかげで自動で
admin.site.register(Person)