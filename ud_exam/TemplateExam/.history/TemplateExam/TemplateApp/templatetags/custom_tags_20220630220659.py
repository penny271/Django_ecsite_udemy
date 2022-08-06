from django import template

register = template.Library()

@register.filter(name='calcute?datetime_')