from django import template

register = template.Library()

@register.filter(name='status_to_string')
def convert_status_to_string(status):
    if status == 10:
        return 'Success'
    elif status == 20:
        return ''