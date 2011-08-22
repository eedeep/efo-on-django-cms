from django.conf.urls.defaults import *

urlpatterns = patterns('',
    url(
        r'^.*$',
        'legacyredirects.views.legacy_redirect',
        name="legacy_redirect"
    ),

)
