from django import template
from app.models import Cart


register = template.Library()


@register.filter(name='total_cart')
def total_cart(Car):
    return len(cart)
