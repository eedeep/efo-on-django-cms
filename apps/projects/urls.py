from django.conf.urls.defaults import *

urlpatterns = patterns('',
    url(
        r'^project/(?P<slug>.*)$',
        'projects.views.project',   
        name="project_view",
    ),
    url(
        r'^$', 
        'projects.views.projects',
        name="projects_projects"
    ),
)