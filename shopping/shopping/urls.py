from django.conf.urls import patterns, include, url
import os
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'shopping.views.home', name='home'),
    # url(r'^shopping/', include('shopping.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    (r'^media(?P<path>.*)$', 'django.views.static.serve', {'document_root': os.path.join(os.path.dirname(__file__), 'static/media')}),
    (r'^static(?P<path>.*)$', 'django.views.static.serve', {'document_root': os.path.join(os.path.dirname(__file__), 'static')}),
    url(r'^$', 'products.views.home'),
    url(r'^products/$', 'products.views.products'),
    url(r'^products/(?P<slug>[-\w]+)/$', 'products.views.product_single'),
    
)
