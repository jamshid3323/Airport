from django import template
from datetime import date

register = template.Library()

today = date.today()


@register.simple_tag()
def get_today():
    d = today.strftime("%Y-%m-%d")
    return d
