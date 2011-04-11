from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool

from django.db.models.manager import ManagerDescriptor

from empcom.cms.plugins.modelcontent.models import ModelContentPlugin
from empcom.util.general import DynamicImport

class CMSModelContentPlugin(CMSPluginBase):
    model = ModelContentPlugin
    name = "Display Some Model Content"
    render_template = ""

    def get_manager_object(self, model_class, manager_class_name):
        for attr, value in model_class.__dict__.iteritems(): #@UnusedVariable
            if(isinstance(value, ManagerDescriptor)):
                if(value.manager.__class__.__name__ == manager_class_name):
                    return value.manager

        raise CMSModelContentPlugin.CouldNotFindSpecifiedManagerOnModel("Could not find the manager '" + manager_class_name + "' on model '" + model_class + "'")

    def render(self, context, instance, placeholder):
        mcd = instance.model_content_descriptor

        pieces = mcd.model_manager.split(':')
        fully_qualified_model_class = pieces[0]
        manager_class = pieces[1]
        model_class = DynamicImport.import_class(fully_qualified_model_class)
         
        manager = self.get_manager_object(model_class, manager_class)
        self.render_template = mcd.template
        
        context.update({'model_collection': manager,
                        'object': instance,
                        'placeholder': placeholder})
        return context

    class CouldNotFindSpecifiedManagerOnModel(Exception):
        def __init__(self, value):
            self.value = value
        def __str__(self):
            return repr(self.value)

plugin_pool.register_plugin(CMSModelContentPlugin)
