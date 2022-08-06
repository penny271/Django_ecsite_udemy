from django import template

register = template.Library()

@register.filter(name='status_to_string')