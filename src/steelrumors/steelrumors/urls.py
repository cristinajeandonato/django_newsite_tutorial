from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

from links.views import LinkListView

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'steelrumors.views.home', name='home'),
    # url(r'^steelrumors/', include('steelrumors.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', LinkListView.as_view(), name='home'),
    url(r'^links/', include('links.urls', namespace="links"))
)
