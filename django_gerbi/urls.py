"""Django page CMS urls module."""

from django.conf.urls.defaults import url, include, patterns
from django.conf.urls.defaults import handler404, handler500
from django_gerbi.views import details
from django_gerbi import settings

if settings.DJANGO_GERBI_USE_LANGUAGE_PREFIX:
    urlpatterns = patterns('',
        url(r'^(?P<lang>[-\w]+)/(?P<path>.*)$', details,
            name='django-gerbi-details-by-path'),
        # can be used to change the URL of the root page
        #url(r'^$', details, name='django-gerbi-root'),
    )
else:
    urlpatterns = patterns('',
        url(r'^(?P<path>.*)$', details, name='django-gerbi-details-by-path'),
        # can be used to change the URL of the root page
        #url(r'^$', details, name='django-gerbi-root'),
    )