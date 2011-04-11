from django import template
from django.contrib.sites.models import Site
from django.template import Context
from django.template.loader import get_template

from programmes.models import Programme

@register.inclusion_tag('programmes/_programme_nav_list.html')
def programme_nav_list():
    """TODO: Need to add ordering here"""
    programmes = Programme.objects.all()

    return { "programmes": programmes}
