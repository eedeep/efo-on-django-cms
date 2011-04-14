import ipdb
from django.core.urlresolvers import reverse, resolve
from django.utils.translation import ugettext_lazy as _

from menus.base import Modifier
from menus.base import NavigationNode
from menus.menu_pool import menu_pool
from cms.menu_bases import CMSAttachMenu

from zinnia.models import Entry
from zinnia.models import Category

class FlatBlogCategoryMenu(CMSAttachMenu):
    """Menu for the categories"""
    name = _('Flat Blog Category Menu')

    def get_nodes(self, request):
        """Return menu's node for categories"""
        nodes = []
        for category in Category.objects.all():
            nodes.append(NavigationNode(category.title,
                                        category.get_absolute_url(),
                                        category.pk, attr={'blog-category':True}))
        return nodes

class FlatBlogCategoryModifier(Modifier):
    """Menu Modifier for flat blog category menu. 
    The purpose of this modified is to make sure the category leaf
    node in the menu still gets highlighted when a blog entry is 
    displayed. """

    def is_blog_entry(self, kwargs):
        """
        If the below if statement is true then we know the request must
        be for a blog entry and not just for a category or a tag or author
        """ 
        if 'queryset' in kwargs and 'year' in kwargs and \
            'month' in kwargs and 'day' in kwargs and 'slug' in kwargs:
            return True
        return False

    def in_blog_menu_tree(self, node):
        if node.attr.get('blog-category') or self.is_top_level_blog_node(node):
            return True
        return False

    def is_blog_request(self, request):
        if request.path.lower().startswith('/blog'):
            return True
        return False

    def is_top_level_blog_node(self, node):
        if node.url.strip('/').lower() == 'blog':
            return True
        return False
        
    def modify(self, request, nodes, namespace, root_id, post_cut, breadcrumb):
        """Modify nodes of a menu"""
        if breadcrumb:
            return nodes

        if self.is_blog_request(request):
            for node in nodes:
                """
                We only want to bother checking this if we're actually somewhere
                in the blog section of the menu tree
                """
                if self.in_blog_menu_tree(node):
                    func, args, kwargs = resolve(request.path)
                    if self.is_blog_entry(kwargs): 
                        """
                        Then try to match the blog category nav node
                        with the the primary category of the blog entry
                        """
                        entry_categories = kwargs['queryset'][0].categories.all()
                        if len(entry_categories) > 0:
                            primary_category = entry_categories[0]
                            if node.title.lower() == primary_category.slug.lower():
                                node.selected = True
                    else:
                        if 'categories' not in request.path \
                            and self.is_top_level_blog_node(node):
                            """
                            If they're looking at a tag, author or some other blog
                            related thing that is not part of blog sub navigation 
                            bar and is not an entry just make sure 'blog' lights up
                            """
                            node.selected = True

        return nodes

menu_pool.register_menu(FlatBlogCategoryMenu)
menu_pool.register_modifier(FlatBlogCategoryModifier)
