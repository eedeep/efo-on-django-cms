from django.shortcuts import get_object_or_404
from django.shortcuts import render_to_response
from django.shortcuts import redirect
from django.template.context import RequestContext
import re

def legacy_redirect(request):
    target = simple_efo_redirect_target(request)

    return redirect(target, permanent=True)

def simple_efo_redirect_target(request):
    """Our switch branches"""
    def contact():
        return '/contact-us'
    def about():
        return '/about-us'
    def previous_projects():
        return '/projects'
    def skills_training():
        return  '/programmes/skills-training'
    def livelihoods():
        return  '/programmes/livelihoods'
    def education():
        return  '/programmes/education'
    def health():
        return  '/programmes/health'
    def home():
        """ This is our default action"""
        return 'landings.views.home'

    """Add more mappings into here if required"""
    mappings = {
                'contact': contact,
                'about': about,
                'about/previous-projects': previous_projects,
                'projects/skills-training-university-based-solar-electricity-courses': skills_training,
                'projects/development-and-livelihoods-community-charging-stations': livelihoods,
                'projects/education-power-systems-for-secondary-schools': education, 
                'projects/health-electricity-for-rural-health-centres': health,
               }

    return mappings.get(request.path.strip('/').lower(), home())()
