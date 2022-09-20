from django import template
from news.models import Categories
from django.db.models import Count, F
from django.core.cache import cache

register = template.Library()


@register.simple_tag
def get_categories():
    categories = cache.get('categories')

    if not categories:
        categories = Categories.objects.annotate(
            cnt=Count('get_news', filter=F('get_news__is_published'))
        ).filter(cnt__gt=0)
        cache.set('categories', categories, 60)

    return categories
