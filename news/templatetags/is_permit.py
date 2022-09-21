from django import template
from django.conf import settings
register = template.Library()


@register.filter(name='group')
def group(u):
    groups = settings.GROUPS_PERMIT_ADD_NEWS
    return u.groups.filter(name__in=groups).exists()