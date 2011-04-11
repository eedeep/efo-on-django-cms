import os

from django.conf import settings
from django.contrib.auth.models import User
from django.db import models
from filebrowser.fields import FileBrowseField

from modelmixins.models import AuditedModel, SluggedModel

class Image(AuditedModel, SluggedModel, models.Model):
    """
    A very simple Image model.
    """
    slide_show = models.BooleanField(
        "Include this image in the slideshow", 
        default=True)
    image = FileBrowseField(
        "Image file", 
        blank=True,
        directory="images/", 
        max_length=200,
        null=True,
        help_text="Click thumbnail to view ful size image.")
    caption = models.TextField(
        null=False)
    photographer = models.CharField(
        blank=True,
        max_length=200,
        help_text="Who took the photo, if that's important to know.")
    order = models.PositiveSmallIntegerField(
        "Order",
        blank=True,
        null=True)
    feature = models.BooleanField(
        help_text="Make this image the 'feature' image")

    class Meta:
        ordering = ['order']
    
    def slug_from_field(self):
        return self.caption

    def __unicode__(self):
        return u'%s' % (self.image)
        

# South requires custom fields to be given "rules".
# See http://south.aeracode.org/docs/customfields.html
if "south" in settings.INSTALLED_APPS and "filebrowser" in settings.INSTALLED_APPS:
    try:
        from filebrowser.fields import FileBrowseField
        from south.modelsinspector import add_introspection_rules
        add_introspection_rules(rules=[((FileBrowseField,), [], {})],
                                      patterns=["filebrowser\.fields\."])
    except ImportError:
        pass
