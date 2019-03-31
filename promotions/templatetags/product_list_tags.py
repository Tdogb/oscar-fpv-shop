from django import template
from django.template.loader import get_template
from catalogue.templatetags import category_tags
from oscar.core.loading import get_model
from oscar.views.generic import ObjectLookupView
from django.shortcuts import render

register = template.Library()
Product = get_model('catalogue', 'Product')
ProductCategory = get_model('catalogue', 'ProductCategory')

@register.simple_tag(takes_context=True)
def product_list(context, category):
    productsInCategories = ProductCategory.objects.filter(category=category)
    products = []
    for i in range(len(productsInCategories)):
        products.append(productsInCategories[i].product)
    template = get_template('promotions/homeproductlist.html')
    request = context['request']
    dictionary = {
        'request': request,
        'products': products,
        'promotion': category.name
    }
    print(dictionary)
    return template.render(request= request, context=dictionary)
