from django.contrib import admin
from .models import Person

# Register your models here.
#- 拡張機能のおかげで自動で転記されるが、実際は
admin.site.register(Person)