import ipdb
from menus.base import NavigationNode
from menus.menu_pool import menu_pool
from django.utils.translation import ugettext_lazy as _
from cms.menu_bases import CMSAttachMenu
from django.core.urlresolvers import reverse

from programmes.models import Programme

class ProjectsMenu(CMSAttachMenu):

    name = _("Projects Menu")

    def get_nodes(self, request):
        nodes = []
        programmes = Programme.objects.all()

        i=0
        for programme in programmes:
            i=i+1 
            node = NavigationNode(_(programme.name), \
                                  reverse('projects_by_programme_view', \
                                            kwargs={'programme_slug': programme.slug}),
                                  i)
                                                    
            nodes.append(node)
        
        return nodes

menu_pool.register_menu(ProjectsMenu)
