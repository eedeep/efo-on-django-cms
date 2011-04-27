import ipdb
from django.shortcuts import render_to_response
from django.shortcuts import get_object_or_404
from django.shortcuts import get_list_or_404
from django.template.context import RequestContext
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from django.db.models import Q

from popularity.signals import view

def people(request):
    programme_staff = User.objects.filter(groups__name__contains='Programme Staff')
    canadian_directors = User.objects.filter(groups__name__contains='Canadian Directors')
    australian_directors = User.objects.filter(groups__name__contains='Australian Directors')
    return render_to_response(
        'people/people.html',
        {
            "programme_staff": programme_staff,
            "canadian_directors": canadian_directors,
            "australian_directors": australian_directors,
        },
        context_instance=RequestContext(request))
