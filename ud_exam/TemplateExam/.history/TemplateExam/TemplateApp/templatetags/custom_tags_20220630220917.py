from django import template
from datetime import datetime #日付から文字列にするのに用いる

register = template.Library()

@register.filter(name='calculate_datetime_to_now')
def calculate_datetime_to_now(value):
    join_datetime = datetime.strptime(value, '')
