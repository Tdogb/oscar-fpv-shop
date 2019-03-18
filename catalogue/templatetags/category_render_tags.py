from django import template
from django.template.loader import get_template
from django.template.loader import select_template
from oscar.core.loading import get_model

register = template.Library()
# Category = get_model('catalogue', 'category')

@register.simple_tag(takes_context=True)
def render_category(context, category, url):
    if not category:
        return ''
    # context['url'] = category.get_absolute_image_url()
    names = 'catalogue/partials/category.html'
    template_ = get_template(names)
    context = context.flatten()

    # Ensure the passed product is in the context as 'product'
    context['category'] = category
    context['url'] = url

    # print("context['category']")
    # print(category)
    return template_.render(context)