import re

from django.template.loader import render_to_string
from cms.utils.placeholder import get_page_from_placeholder_if_exists

from empcom.util.regex import in_admin_regex

def content_finaliser(instance, placeholder, rendered_content, original_context):
    '''
    This plugin processor displays the tag legend on the allowed 
    plugins specified below in the admin interface.
    '''
    
    # This plugin processor only acts in the admin site ..
    if not re.match(in_admin_regex, original_context['request'].path):
        return rendered_content
    
    taggable_plugins = ['TemplateTextPlugin', 'TemplateSnippetPlugin']
    
    # .. and only on certain plugins.
    if not instance.plugin_type in taggable_plugins:
        return rendered_content
    
    # OK, so we're in the admin mode of a templatable plugin - so we wrap the plugin
    # interface with a handy tag legend.
     
    tag_list_template = 'cms/admin/tag_list_box.html'             
    context_dictionary = {
        'content': rendered_content,
        'tagList': get_tag_list(get_page_from_placeholder_if_exists(instance.placeholder))
        }        
    return render_to_string(tag_list_template, context_dictionary)

class __TagList(object):
    def __init__(self, private_tags=[], inheritable_tags=[]):
        self.private_tags       = private_tags
        self.inheritable_tags   = inheritable_tags

#TODO: Figure out where these should go.
__page_tags = {
    'home':                         __TagList(('private_tag_home',), ('inheritable_tag_home',)),
    'home/redeem/cash':             __TagList(('private_tag_cash',), ('inheritable_tag_cash',)),
    'home/redeem/cash/redeem-x':    __TagList(('private_tag_redeem-x',), ('inheritable_tag_redeem-x',)),
    }

def get_tag_list(page, only_inheritable=False):
    """ Return a list of tags for this page, and inheritable tags from parent pages """
    # Some plugins are not associated with a page.
    #TODO: Which? Snippet?    
    if not page:
        return []
    
    tag_list = []
    
    # If the page has a parent, grab it's inheritable tags before adding our own. 
    if page.parent: 
        tag_list.extend(get_tag_list(page.parent, True))
    
    # Now, extract any inheritable (and possibly private) tags for the page identified by the cms path page.get_path()    
    try:
        # May raise key error.
        page_tags = __page_tags[page.get_path()]
        
        if only_inheritable:
            tag_list.extend(page_tags.inheritable_tags)
        else:
            tag_list.extend(page_tags.inheritable_tags)
            tag_list.extend(page_tags.private_tags)
    except KeyError:
        # No matter, there are no tags defined for this page.
        pass
    
    return tag_list

