from django.conf.urls.defaults import *

urlpatterns = patterns('',
    url(
        r'^(?P<slug>.*)$',
        'programmes.views.programme',   
        name="programme_view",
    ),
    url(
        r'^$', 
        'programmes.views.programmes',
        name="programmes_programmes"
    ),
)
