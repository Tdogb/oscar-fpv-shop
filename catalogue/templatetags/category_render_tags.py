from django import template
from django.template.loader import get_template
from django.template.loader import select_template
from oscar.core.loading import get_model

register = template.Library()
Category = get_model('catalogue', 'category')

@register.simple_tag(takes_context=True)
def render_category(context, category):
    if not category:
        return ''
    template_ = get_template('catalogue/partials/category.html')
    context = context.flatten()

    # Ensure the passed product is in the context as 'product'
    context['category'] = category
    return template_.render(context)