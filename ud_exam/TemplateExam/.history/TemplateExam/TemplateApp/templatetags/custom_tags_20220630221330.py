from django import template
from datetime import datetime #日付から文字列にするのに用いる
import math

register = template.Library()

@register.filter(name='calculate_datetime_to_now')
def calculate_datetime_to_now(value):
    #文字列からdatetime型に変換できる
    join_datetime = datetime.strptime(value, '%Y/%m/%d')
    now_datetime = datetime.now()
    # timedelta class
    diff_datetime = now_datetime - join_datetime
    diff_days = diff_datetime.days
    diff_years = math.floor(diff_days / 365)
    diff_months = math.floor((diff_days - 365 * diff_years) / 30)