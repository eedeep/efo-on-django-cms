from django.conf.urls.defaults import *
from django.contrib import admin
from django.conf import settings

admin.autodiscover()

#an inconsequential change
urlpatterns = patterns('',
#    url(r'^admin_tools/', include('admin_tools.urls')),
    url(r'^tinymce/', include('tinymce.urls')),
    url(r'^admin/filebrowser/', include('filebrowser.urls')),
    url(r'^filebrowser/', include('filebrowser.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include('cms.urls')),
)

if settings.DEBUG:
    urlpatterns = patterns('',
        (r'^' + settings.MEDIA_URL.lstrip('/'), include('appmedia.urls')),
    ) + urlpatterns

if settings.SERVE_MEDIA:
    urlpatterns += patterns("",
       url(r"", include("staticfiles.urls")),
       )
