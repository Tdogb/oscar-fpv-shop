from django import template
from catalogue.templatetags import category_tags
from oscar.core.loading import get_model

register = template.Library()

@register.simple_tag(name='product_list')
def product_list():
    print("test")
    # categories = category_tags.get_annotated_list(depth=2)
    # for category,info in categories:
    #     print(category)
    hival = 'Hi'
    return hival