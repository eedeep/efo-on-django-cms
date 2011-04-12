from django.conf.urls.defaults import *
from django.contrib import admin
from django.conf import settings

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^tinymce/', include('tinymce.urls')),
    url(r'^admin/filebrowser/', include('filebrowser.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include('cms.urls')),
    url(r"^members/", include("profiles.urls")),
    url(r"^account/logout/$", 
        "pinax_local.apps.account.views.logout",
        {
            "template_name": "account/logout.html",
            "next_page": "/"
        }, name="logout"),
    url(r"^search/", include("search.urls")),
)

if settings.DEBUG:
    urlpatterns = patterns('',
        (r'^' + settings.MEDIA_URL.lstrip('/'), include('appmedia.urls')),
    ) + urlpatterns

if settings.SERVE_MEDIA:
    urlpatterns += patterns("",
       url(r"", include("staticfiles.urls")),
       )
