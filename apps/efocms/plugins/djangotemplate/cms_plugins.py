import os
from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool

from django.conf import settings

from empcom.cms.plugins.djangotemplate.models import DjangoTemplatePlugin


class CMSDjangoTemplatePlugin(CMSPluginBase):
    model = DjangoTemplatePlugin 
    name = "Display A Django Template"
    render_template = ""

    def render(self, context, instance, placeholder):
        self.render_template = os.path.join(settings.PROJECT_PATH, \
                                                instance.template)

        context.update({'model_collection': instance,
                        'object': instance,
                        'placeholder': placeholder})
        return context

plugin_pool.register_plugin(CMSDjangoTemplatePlugin)
