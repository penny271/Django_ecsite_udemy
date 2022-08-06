from django.contrib import admin
from .models import Person

# Register your models here.
#- 拡張機能のおかげで自動で転記されるが、実際は手動で追記しないと管理画面に反映されないconda activate djangoenv

admin.site.register(Person)