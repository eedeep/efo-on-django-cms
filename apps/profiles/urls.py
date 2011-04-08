from django.conf.urls.defaults import *

urlpatterns = patterns('',
    url(
        r'^$', 
        'profiles.views.profiles',
        name="profiles_list"
    ),
    url(
        r'^account/$',
        'profiles.views.account',   
        name="profile_account",
    ),
    url(
        r'^(?P<username>[\w\._-]+)/$',
        'profiles.views.profile',
        name="profile_view",
    )
)