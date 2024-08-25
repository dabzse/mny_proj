from django import template
from ..models import LearnPlace

register = template.Library()

@register.filter
def get_place_name(learn_places, filter_by):
    if filter_by == 'sl':
        return learn_places.get(id=1).name
    elif filter_by == 'gh':
        return learn_places.get(id=2).name
    elif filter_by == 'ud':
        return learn_places.get(id=3).name
    return "All"
