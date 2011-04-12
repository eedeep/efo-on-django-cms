from django import template
from django.contrib.sites.models import Site
from django.template import Context
from django.template.loader import get_template

from features.models import Feature, FeatureSet, SiteFeatureArea
from features.utils import get_features
from articles.models import Article


register = template.Library()

@register.inclusion_tag('base/_asides_object_list.html')
def site_features():

    objects = []
    for hf in get_features('home'):
        objects.append(hf.content_object)
    
    return { 
        'objects': objects,
    }