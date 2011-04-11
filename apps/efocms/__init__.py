from menus.base import Modifier
from menus.menu_pool import menu_pool

""" 
request.breadcrumb_selected_node = '/redeem/cash/redeem-x/purchase-receipt/'
request.breadcrumb_node_changes = {
    '/redeem/cash/redeem-x/': {
        'title': 'Redeem $%s' % cash_value,
        'url': '/redeem/cash/%s/' % cash_value,
        },
    }
"""

class BreadcrumbModifier(Modifier):
    """
    
    """
    def modify(self, request, nodes, namespace, root_id, post_cut, breadcrumb):
        if not breadcrumb:
            return nodes
        
        modify_selected = hasattr(request, 'breadcrumb_selected_node')
        modify_nodes    = hasattr(request, 'breadcrumb_node_changes')
        if modify_selected or modify_nodes:
            for node in nodes:
                if modify_selected:
                    if node.url == request.breadcrumb_selected_node:
                        node.selected = True
                    else:
                        node.selected = False
                
                if modify_nodes and node.url in request.breadcrumb_node_changes:
                    node_change = request.breadcrumb_node_changes[node.url]
                    if 'title' in node_change:
                        node.title = node_change['title']
                    if 'url' in node_change:
                        node.url = node_change['url']
                    
        return nodes
    
def modifies_breadcrumb(func):
    def breadcrumb_modify_decorator(*args, **kwargs):        
        menu_pool.modifiers.append(BreadcrumbModifier)
        result = func(*args, **kwargs)
        menu_pool.modifiers.remove(BreadcrumbModifier)
        return result
    return breadcrumb_modify_decorator