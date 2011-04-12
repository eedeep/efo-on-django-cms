from menus.base import Modifier
from menus.menu_pool import menu_pool

class GlobalMenuModifier(Modifier):
    """
    If the user is logged in, remove certain menu options.
    
    Django cms provides a way to hide an option from a non logged in user, but no
    way to hide something from someone who is logged in. This menu modifier adds
    this capability.
    """
    
    def modify(self, request, nodes, namespace, root_id, post_cut, breadcrumb):
        # We don't modify the breadcrumb, and we also wait until the post_cut
        # phase so that we process a potentially smaller node tree.
        # See http://www.3lance.lv/django-cms/app_integration.html        
        if breadcrumb or not post_cut or not request.user.is_authenticated():
            return nodes
                
        trim_nodes = ['/login/', '/register/']
        
        return filter(lambda node: node.url not in trim_nodes, nodes)
    
menu_pool.register_modifier(GlobalMenuModifier)