# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function, unicode_literals

from cms.sitemaps import CMSSitemap
from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.i18n import i18n_patterns
from django.contrib import admin
from django.contrib.sitemaps.views import sitemap
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.views.static import serve
from polls import views

admin.site.site_header = 'Environmental Portal'
admin.site.site_title = 'Environmental Portal'
admin.site.index_title = 'Environmental Portal'
admin.autodiscover()

urlpatterns = [
  url(r'^sitemap\.xml$', sitemap, {'sitemaps': {'cmspages': CMSSitemap}})
]

urlpatterns += i18n_patterns(
  url(r'^admin/', include(admin.site.urls)),  # NOQA
  url(r'^accounts/', include('registration.backends.simple.urls')),
  url(r'^polls/', include('polls.urls', namespace='polls')),
  url(r'^survey/', include('cmsplugin_survey.urls')),
  url(r'^survey_results/', include('survey_results.urls')),
  # url(r'^saq/', include('cms_saq.urls')),
  url(r'^', include('cms.urls'))
)

# This is only needed when using runserver.
if settings.DEBUG:
  urlpatterns = [
    url(r'^media/(?P<path>.*)$', serve,
      {'document_root': settings.MEDIA_ROOT, 'show_indexes': True})
  ] + staticfiles_urlpatterns() + urlpatterns
