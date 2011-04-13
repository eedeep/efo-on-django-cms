from django.conf.urls.defaults import *

urlpatterns = patterns('',
    url(
        r'^$', 
        'programmes.views.programmes',
        name="programmes_view"
    ),
    url(
        r'^(?P<slug>.*)$',
        'programmes.views.programme',   
        name="programme_view",
    ),
)
