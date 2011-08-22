from django.conf.urls.defaults import *

urlpatterns = patterns('',
    url(
        r'^.*$',
        'legacyblogredirects.views.legacy_blog_entry_redirect',
        name="legacy_blog_entry_redirect"
    ),

)
