from django.conf.urls.defaults import *

urlpatterns = patterns('',
    url(
        r'^$', 
        'donors.views.donors',
        name="donors_view"
    ),
)
