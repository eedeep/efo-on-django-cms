import ipdb
from django.shortcuts import render_to_response
from django.shortcuts import get_object_or_404
from django.shortcuts import get_list_or_404
from django.template.context import RequestContext
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.db.models import Q

from donors.models import Donor

from popularity.signals import view

def donors(request):
    donors = Donor.objects.all()
    return render_to_response(
        'donors/donors.html',
        {
            "donors": donors
        },
        context_instance=RequestContext(request))
