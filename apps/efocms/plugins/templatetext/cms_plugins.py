from cms.plugin_pool import plugin_pool
from cms.plugins.text.cms_plugins import TextPlugin
from cms.plugins.text.utils import plugin_tags_to_user_html

from django.utils.translation import ugettext_lazy as _
from django.template import Template
from django.conf import settings

class TemplateTextPlugin(TextPlugin):
    """
    Basically this is just the text plugin but done in such a way as to treat
    the text as a django template.
    """
    name = _("Template Text")
    render_template = None

    def render(self, context, instance, placeholder):
        if settings.CMS_DBGETTEXT:
            from dbgettext.parser import parsed_gettext #@UnresolvedImport
            instance.body = parsed_gettext(instance, 'body')
            
        context.update({
            'body': plugin_tags_to_user_html(instance.body, context, placeholder),
            'placeholder': placeholder,
            'object': instance
        })
        
        self.render_template = Template(instance.body)
        return context

plugin_pool.register_plugin(TemplateTextPlugin)
