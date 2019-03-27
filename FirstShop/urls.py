from django.conf.urls import include, url
from django.contrib import admin
from oscar.app import application as shop
from paypal.express.dashboard.app import application
from django.utils.translation import ugettext_lazy as _
from oscar.defaults import OSCAR_DASHBOARD_NAVIGATION
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.views.static import serve
from django.urls import re_path


OSCAR_DASHBOARD_NAVIGATION.append(
    {
        'label': _('PayPal'),
        'icon': 'icon-globe',
        'children': [
            {
                'label': _('Express transactions'),
                'url_name': 'paypal-express-list',
            },
        ]
    })

urlpatterns = [

    url(r'^i18n/', include('django.conf.urls.i18n')),

    # The Django admin is not officially supported; expect breakage.
    # Nonetheless, it's often useful for debugging.
    url(r'^admin/', admin.site.urls),
    url(r'^checkout/paypal/', include('paypal.express.urls')),
    url(r'^dashboard/paypal/express/', application.urls),
    url(r'^static/(?P<path>.*)$', serve), re_path(r'^static/(?P<path>.*)$', serve, {'document_root': settings.STATIC_ROOT, }),
    url(r'', shop.urls),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
# if settings.LOCAL:
    # urlpatterns += url(r'^static/(?P<path>.*)$', serve), re_path(r'^static/(?P<path>.*)$', serve, {'document_root': settings.STATIC_ROOT, }),

# urlpatterns += url(r'', shop.urls),