import ipdb
from django.shortcuts import render_to_response
from django.shortcuts import get_object_or_404
from django.shortcuts import get_list_or_404
from django.template.context import RequestContext
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

from popularity.signals import view

def sent(request):
    return render_to_response(
        'membrete/sent.html',
        context_instance=RequestContext(request))
