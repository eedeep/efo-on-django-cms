import ipdb
from menus.base import NavigationNode
from menus.menu_pool import menu_pool
from django.utils.translation import ugettext_lazy as _
from cms.menu_bases import CMSAttachMenu
from programmes.models import Programme

class ProgrammesMenu(CMSAttachMenu):

    name = _("Programmes Menu")

    def get_nodes(self, request):
        nodes = []
        programmes = Programme.objects.all()

        i=0
        for programme in programmes:
            i=i+1 
            node = NavigationNode(_(programme.name), programme.get_absolute_url(), i)
            nodes.append(node)
        
        return nodes

menu_pool.register_menu(ProgrammesMenu)
