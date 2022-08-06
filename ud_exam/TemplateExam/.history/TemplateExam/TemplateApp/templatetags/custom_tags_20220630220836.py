from django import template
from datetime import datetime

register = template.Library()

@register.filter(name='calculate_datetime_to_now')
def calculate_datetime_to_now(value):
