from django.shortcuts import render_to_response
from django.shortcuts import get_object_or_404
from django.shortcuts import get_list_or_404
from django.template.context import RequestContext
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

from popularity.signals import view
from projects.models import Project

def index(request):
    
    projects = Project.objects.all()
    
    return render_to_response(
        'projects/index.html',
        {
            "projects": projects,
        },
        context_instance=RequestContext(request))
        
def project(request, project_id=None, slug=None,):
    
    project = get_object_or_404(
        Project,
        slug=slug)
        
    view.send(project)

    return render_to_response(
        'projects/project.html',
        {
            "project": project,
        },
        context_instance=RequestContext(request))
        
def projects(request):
    
    projects = Project.objects.all()
    
    return render_to_response(
        'projects/projects.html',
        {
            "projects": projects,
        },
        context_instance=RequestContext(request))
