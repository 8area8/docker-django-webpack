"""Main URL Configuration."""

from django.conf import settings
from django.urls import path, include
from django.contrib import admin

from django_otp.admin import OTPAdminSite


# Django urls
# https://docs.djangoproject.com/fr/2.1/topics/http/urls/

urlpatterns = [
    # Customized admin path
    path('lch_admin/', admin.site.urls),
    # Personal views
    path('', include('home.urls')),
]

# Debug-toolbar part
# https://django-debug-toolbar.readthedocs.io/en/latest/installation.html

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += [path('__debug__/', include(debug_toolbar.urls))]

#  Admin rename and security
# https://hackernoon.com/5-ways-to-make-django-admin-safer-eb7753698ac8

admin.site.site_header = 'La Crèche Humaniste - Administration'
admin.site.site_title = 'La Crèche Humaniste'
admin.site.__class__ = OTPAdminSite
