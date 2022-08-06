from django import template

register = template.Library()

@register.filter(name='calcudatetime_')