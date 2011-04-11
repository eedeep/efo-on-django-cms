from django.shortcuts import render_to_response
from django.shortcuts import get_object_or_404
from django.shortcuts import get_list_or_404
from django.template.context import RequestContext
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

from base.utils import filter_by_getvalues
from popularity.signals import view

from programmes.models import Programme

def index(request):
    
    programmes = Programme.objects.all()
    
    return render_to_response(
        'programmes/index.html',
        {
            "programmes": programmes,
        },
        context_instance=RequestContext(request))
        
def programme(request, programme_id=None, slug=None,):
    
    programme = get_object_or_404(
        Programme,
        slug=slug)
        
    view.send(programme)

    return render_to_response(
        'projects/project.html',
        {
            "programme": programme,
        },
        context_instance=RequestContext(request))
        
def programmes(request):
    
    programmes = Programme.objects.all()
    
    return render_to_response(
        'projects/projects.html',
        {
            "programmes": programmes,
        },
        context_instance=RequestContext(request))
