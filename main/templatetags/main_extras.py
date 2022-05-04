from django import template
from main.models import *
register = template.Library()


@register.simple_tag(name='getcats')
def get_categories(filter=None):
    if not filter:
        return Categories.objects.all()
    else:
        return Categories.objects.filter(pk=filter)


@register.inclusion_tag('main/list_categories.html')
def show_categories(sort=None,cat_selected=0):
    if not sort:
        cats=Categories.objects.all()
    else:
        cats=Categories.objects.order_by(sort)
        return {'cats':cats,'cat_selected':cat_selected}