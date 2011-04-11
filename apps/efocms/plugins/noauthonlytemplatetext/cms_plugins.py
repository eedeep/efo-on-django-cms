from cms.plugin_pool import plugin_pool

from django.utils.translation import ugettext_lazy as _
from django.template import Template
from django.contrib.auth.models import AnonymousUser

from empcom.cms.plugins.templatetext.cms_plugins import TemplateTextPlugin

class NoAuthOnlyTemplateTextPlugin(TemplateTextPlugin):
    """
    Basically this is just the text plugin but done in such a way as to treat
    the text as a django template.
    """
    name = _("No Auth Only Template Text")

    def render(self, context, instance, placeholder):
        if(isinstance(context['request'].user, AnonymousUser)):
            self.render_template = Template(instance.body)
        else:
            self.render_template = Template('')

        return super(NoAuthOnlyTemplateTextPlugin, self).render(context, instance, placeholder)


plugin_pool.register_plugin(NoAuthOnlyTemplateTextPlugin)
