import ipdb
from django.shortcuts import render_to_response
from django.shortcuts import get_object_or_404
from django.shortcuts import get_list_or_404
from django.template.context import RequestContext
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

from popularity.signals import view

from programmes.models import Programme

def programmes(request):
    programmes = Programme.objects.all()
    return render_to_response(
        'programmes/programmes.html',
        {
            "programmes": programmes,
            "p_health": programmes.filter(slug='health')[0] if programmes.filter(slug='health') else None,
            "p_education": programmes.filter(slug='education')[0] if programmes.filter(slug='education') else None,
            "p_skillstraining": programmes.filter(slug='skills-training')[0] if programmes.filter(slug='skills-training') else None,
            "p_livelihoods": programmes.filter(slug='livelihoods')[0] if programmes.filter(slug='livelihoods') else None
        },
        context_instance=RequestContext(request))

def programme(request, slug=None):
    programme = get_object_or_404(
        Programme,
        slug=slug.rstrip('/'))

    view.send(programme)

    return render_to_response(
        'programmes/programme.html',
        {
            "programme": programme,
        },
        context_instance=RequestContext(request))
