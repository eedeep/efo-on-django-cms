from django.conf.urls.defaults import *

urlpatterns = patterns('',
    url(
        r'^$', 
        'home.views.home',
        name="home_view"
    ),
)
