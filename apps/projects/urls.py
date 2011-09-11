from django.conf.urls.defaults import *

urlpatterns = patterns('',
    url(
        r'^$', 
        'projects.views.projects',
        name="projects_view"
    ),
    url(
        r'^by-programme/(?P<programme_slug>.*)$',
        'projects.views.projects_by_programme',   
        name="projects_by_programme_view",
    ),
    url(
        r'^(?P<slug>.*)/$',
        'projects.views.project',   
        name="project_view",
    ),
)
