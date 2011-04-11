from django.contrib import admin
from django.db import models
from django.conf import settings

from cms.models import CMSPlugin

from empcom.fields.models import \
    AutoDateCreatedField, AutoLastModifiedField, \
    PositiveBigIntegerAutoField

def get_template_choices():
    choices = {}
    for template_path, display_name in settings.DISPLAYABLE_TEMPLATES.items():
        choices[template_path] = template_path + ' [' + display_name + ']'

    return choices.items()


class DjangoTemplateDescriptor(models.Model):
    """
    Models the cash amounts that can be redeemed by members.
    """
    id = PositiveBigIntegerAutoField(primary_key=True)
    template = models.CharField(max_length=1000, \
            choices=get_template_choices())

    date_created = AutoDateCreatedField()
    last_modified = AutoLastModifiedField()

    def __unicode__(self):
        return self.descriptor_name

    class Admin:
        pass


class DjangoTemplateDescriptorAdmin(admin.ModelAdmin):
    pass
admin.site.register(DjangoTemplateDescriptor, DjangoTemplateDescriptorAdmin)


class DjangoTemplatePlugin(CMSPlugin):
    template = models.CharField(max_length=1000, \
            choices=get_template_choices())
