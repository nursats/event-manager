from django import template

from events.models import Categories

register = template.Library()

@register.simple_tag()
def tag_categories():
    all_category = Categories.objects.filter(slug='all').first()
    if all_category:
        other_categories = Categories.objects.exclude(id=all_category.id)
        return [all_category] + list(other_categories)
    else:
        return Categories.objects.all()