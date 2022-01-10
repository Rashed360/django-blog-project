from django import template

register = template.Library()

def value_range(value,range):
    if len(value) > range:
        return value[0:range-3]+'...'
    else:
        return value


register.filter('value_range', value_range)