import ipdb
from django.shortcuts import render_to_response
from django.shortcuts import get_object_or_404
from django.shortcuts import get_list_or_404
from django.template.context import RequestContext
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

from popularity.signals import view
from projects.models import Project

def projects(request):
    projects = Project.objects.order_by('-date_finished')
    return render_to_response(
        'projects/projects.html',
        {
            "projects": projects,
        },
        context_instance=RequestContext(request))

def project(request, slug):
    project = Project.objects.get(slug=slug.strip('/'))
    view.send(project)

    return render_to_response(
        'projects/project.html',
        {
            "project": project,
        },
        context_instance=RequestContext(request))

def projects_by_programme(request, programme_slug):
    projects = Project.objects.filter(programme__slug=programme_slug.strip('/')).order_by('-date_finished')
    return render_to_response(
        'projects/projects.html',
        {
            "projects": projects,
        },
        context_instance=RequestContext(request))
