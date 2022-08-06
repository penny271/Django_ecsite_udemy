from django.contrib import admin
#- 管理画面の表示の仕方を変えたい場合に使用
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth import get_user_model
from .forms import UserChangeForm, UserCreationForm
# from .models import Students, Schools

#- get_user_model()は現在使用しているアプリケーションのUserのモデルを返す
# 今回、ROOT_URLCONF = 'CustomizedUser.urls'を使っているのでそれが返ってくる
User = get_user_model()

#- 管理画面の表示の仕方を変えたい場合に使用
# class CustomizeUserAdmin(UserAdmin):
#     form = UserChangeForm # ユーザ編集画面で使うForm
#     add_form = UserCreationForm # ユーザ作成画面

#     # 一覧画面で表示
#     list_display = ('username', 'email', 'is_staff')

#     # ユーザ編集画面で表示する要素
#     fieldsets = (
#         ('ユーザ情報', {'fields': ('username', 'email', 'password', 'website', 'picture')}),
#         ('パーミッション', {'fields': ('is_staff', 'is_active', 'is_superuser')}),
#         )

#     # ユーザ作成画面
#     add_fieldsets = (
#         ('ユーザ情報', {
#             'fields':('username', 'email', 'password', 'confirm_password')
#         }),
#     )

# admin.site.register(User, CustomizeUserAdmin)
# admin.site.register(Students)
# admin.site.register(Schools)

# @admin.register(Students) # registerしている
# class StudentAdmin(admin.ModelAdmin):
#     fields = ('name', 'score', 'age', 'school')
#     list_display = ('id','name', 'age', 'score', 'school')
#     list_display_links = ('id',)
#     search_fields = ('name',)
#     list_filter = ('name','age', 'score', 'school')
#     #- 編集リンクが設定されているコラムは指定できず、エラーになる
#     list_editable = ('name', 'age', 'score','school')

# @admin.register(Schools)
# class SchoolsAdmin(admin.ModelAdmin):
#     list_display = ('name', 'student_count')

#     #- objはSchoolsAdminの画面上に表れている一つ一つの
#     #- インスタンスをobjととしてとっている
#     def student_count(self, obj):
#         print(type(obj))
#         #- どういうメソッドやプロパティをもっているか確認するのに
#         #- dir()はとても便利!
#         print(dir(obj))
#         count = obj.students_set.count()
#         return count

#     student_count.short_description = '生徒数'