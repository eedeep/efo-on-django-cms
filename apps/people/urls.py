from django.conf.urls.defaults import *

urlpatterns = patterns('',
    url(
        r'^$', 
        'people.views.people',
        name="people_view"
    ),
)
