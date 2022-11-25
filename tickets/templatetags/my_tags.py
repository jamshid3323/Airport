from django import template
from datetime import date

register = template.Library()

today = date.today()


@register.simple_tag()
def get_today():
    d = today.strftime("%Y-%m-%d")
    return d


@register.simple_tag()
def max_age():
    y = today.year - 18
    return f"{y}-{today.month}-{today.day}"
