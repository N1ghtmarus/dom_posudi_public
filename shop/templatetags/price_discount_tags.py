from atexit import register
from django import template


register = template.Library()

@register.simple_tag
def price_discount(price, sale):
    return price - (price * sale / 100)