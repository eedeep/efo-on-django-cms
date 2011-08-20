import ipdb
from menus.base import Modifier
from menus.base import NavigationNode
from menus.menu_pool import menu_pool
from django.utils.translation import ugettext_lazy as _
from cms.menu_bases import CMSAttachMenu
from django.core.urlresolvers import reverse, resolve

from programmes.models import Programme
from projects.models import Project

class ProjectsMenu(CMSAttachMenu):

    name = _("Projects Menu")

    def get_nodes(self, request):
        nodes = []
        programmes = Programme.objects.order_by('display_order')

        i=0
        for programme in programmes:
            i=i+1 
            node = NavigationNode(_(programme.name), \
                                  reverse('projects_by_programme_view', \
                                            kwargs={'programme_slug': programme.slug}),
                                  i)
                                                    
            nodes.append(node)
        
        return nodes

class ProjectsMenuModifier(Modifier):
    """Menu Modifier for the projects menu. 
    The purpose of this modifier is to make sure the programme leaf
    node in the menu still gets highlighted when a blog entry is 
    displayed. """

    def is_project_detail_page_request(self, func):
        if func.__name__ == 'project':
            return True
        return False

    def get_project(self, slug):
       return Project.objects.get(slug=slug)

    def is_projects_menu_leaf_node(self, node):
        ancestors = node.get_ancestors()
        for ancestor in ancestors:
            if ancestor.title.lower() == 'projects':
                return True
        return False
        
    def modify(self, request, nodes, namespace, root_id, post_cut, breadcrumb):
        """Modify nodes of a menu"""
        if breadcrumb:
            return nodes

        func, args, kwargs = resolve(request.path)
        if self.is_project_detail_page_request(func):
            project = self.get_project(kwargs['slug'])
            for node in nodes:
                if project.programme.name.lower() == node.title.lower():
                    if self.is_projects_menu_leaf_node(node):
                        node.selected = True
                else:
                    node.selected = False

        return nodes

menu_pool.register_modifier(ProjectsMenuModifier)
menu_pool.register_menu(ProjectsMenu)
