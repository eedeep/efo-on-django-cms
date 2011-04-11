from django.db import models
from django.utils.translation import ugettext_lazy as _
from cms.models import CMSPlugin
from cms.utils.helpers import reversion_register

# Stores the actual data
class ScheduledSnippet(models.Model):
    """
    A snippet of HTML or a Django template
    """
    name = models.CharField(_("name"), max_length=255, unique=True)
    html = models.TextField(_("html"), blank=True)

    startDateTime = models.DateTimeField()
    endDateTime = models.DateTimeField() 

    def __unicode__(self):
        return self.name

    class Meta:
        ordering = ['name']
        verbose_name = _("ScheduledSnippet")
        verbose_name_plural = _("ScheduledSnippets")
    

# Plugin model - just a pointer to ScheduledSnippet
class ScheduledSnippetPtr(CMSPlugin):
    snippet = models.ForeignKey(ScheduledSnippet)

    class Meta:
        verbose_name = _("ScheduledSnippet")

    search_fields = ('snippet__html',)

    def __unicode__(self):
        # Return the referenced snippet's name rather than the default (ID #)
        return self.snippet.name


# We don't both with ScheduledSnippetPtr, since all the data is actually in ScheduledSnippet
reversion_register(ScheduledSnippet)

