from django.conf.urls import include, url
from django.contrib import admin
from oscar.app import application as shop
from paypal.express.dashboard.app import application

urlpatterns = [
    url(r'^i18n/', include('django.conf.urls.i18n')),

    # The Django admin is not officially supported; expect breakage.
    # Nonetheless, it's often useful for debugging.
    url(r'^admin/', admin.site.urls),
    url(r'^checkout/paypal/', include('paypal.express.urls')),

    url(r'', shop.urls),
]
