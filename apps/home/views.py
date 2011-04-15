import ipdb
from django.shortcuts import render_to_response
from django.shortcuts import get_object_or_404
from django.shortcuts import get_list_or_404
from django.template.context import RequestContext
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from features.utils import get_features

def home(request):
    home_features = get_features('home')

    return render_to_response(
        'home/home.html',
        {
            "home_features": home_features,
        },
        context_instance=RequestContext(request))
