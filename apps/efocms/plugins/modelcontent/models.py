from django.contrib import admin
from django.db import models
from django.db.models.manager import ManagerDescriptor
from django.conf import settings

from cms.models import CMSPlugin

from empcom.fields.models import \
    AutoDateCreatedField, AutoLastModifiedField, \
    PositiveBigIntegerAutoField, PositiveBigIntegerForeignKey

from empcom.util.general import DynamicImport


def get_model_manager_choices():
    choices = {}
    for key in settings.DISPLAYABLE_MODELS:
        model_class = DynamicImport.import_class(key) 
        for attr, value in model_class.__dict__.iteritems():
            if(isinstance(value, ManagerDescriptor) and attr != 'objects'):
                choices[key + ':' + value.manager.__class__.__name__] = \
                            value.manager.__class__.__name__ + ' [' + model_class.__name__ + ']'

    return choices.items()


class ModelContentDescriptor(models.Model):
    """
    Models the cash amounts that can be redeemed by members.
    """
    id = PositiveBigIntegerAutoField(primary_key=True)
    descriptor_name = models.CharField(max_length=255, unique=True)
    model_manager = models.CharField(max_length=1000, \
            choices=get_model_manager_choices())
    template = models.CharField(max_length=255)

    date_created = AutoDateCreatedField()
    last_modified = AutoLastModifiedField()

    def __unicode__(self):
        return self.descriptor_name

    class Admin:
        pass


class ModelContentDescriptorAdmin(admin.ModelAdmin):
    pass
admin.site.register(ModelContentDescriptor, ModelContentDescriptorAdmin)


class ModelContentPlugin(CMSPlugin):
    model_content_descriptor = \
        PositiveBigIntegerForeignKey(ModelContentDescriptor)
