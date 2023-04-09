from django import template
from ..models import Mainmenu

register = template.Library()


@register.inclusion_tag('mysite/../../templates/partials/category_navbar.html')
def category_navbar():
    return{
        'main': Mainmenu.objects.filter(status=True)
    }
