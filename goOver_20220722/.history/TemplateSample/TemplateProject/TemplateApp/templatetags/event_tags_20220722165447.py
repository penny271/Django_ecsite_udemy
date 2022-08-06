from django import template

register = template.Library()

@register.filter(name='status_to_string')
def convert_status_to_string(status,name):
    print(f'name = {name}')
    print(f'n{name=}')
    if status == 10:
        return 'Success'
    elif status == 20:
        return 'Error'
    elif status == 30:
        return 'Pending'
    elif status == 40:
        return 'Failed'
    else:
        return 'ELSE'