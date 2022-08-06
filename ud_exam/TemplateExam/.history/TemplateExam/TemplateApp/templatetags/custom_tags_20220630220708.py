from django import template

register = template.Library()

@register.filter(name='calculate_datetime_')