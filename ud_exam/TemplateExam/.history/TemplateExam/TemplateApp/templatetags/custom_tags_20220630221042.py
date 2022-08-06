from django import template
from datetime import datetime #日付から文字列にするのに用いる

register = template.Library()

@register.filter(name='calculate_datetime_to_now')
def calculate_datetime_to_now(value):
    #文字列からdatetime型に変換できる
    join_datetime = datetime.strptime(value, '%Y/%m/%d')
    now_datetime = datetime.now()
    