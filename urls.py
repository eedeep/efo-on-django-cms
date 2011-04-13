from django.conf.urls.defaults import *
from django.contrib import admin
from django.conf import settings

admin.autodiscover()

if settings.SERVE_MEDIA:
    urlpatterns = patterns("",
       url(r"", include("staticfiles.urls")),
       )

urlpatterns += patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^tinymce/', include('tinymce.urls')),
    url(r'^admin/filebrowser/', include('filebrowser.urls')),
    url(r'^', include('cms.urls')),
    url(r"^programmes/", include("programmes.urls")),
    url(r"^members/", include("profiles.urls")),
    url(r"^account/logout/$", 
        "pinax_local.apps.account.views.logout",
        {
            "template_name": "account/logout.html",
            "next_page": "/"
        }, name="logout"),
    url(r"^search/", include("search.urls")),
    url(r'^blog/', include('zinnia.urls')),
    url(r'^comments/', include('django.contrib.comments.urls')),
)

if settings.DEBUG:
    urlpatterns = patterns('',
        (r'^' + settings.MEDIA_URL.lstrip('/'), include('appmedia.urls')),
    ) + urlpatterns

