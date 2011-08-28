import datetime

from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.comments.models import Comment
from popularity.models import ViewTracker

from modelmixins.models import AuditedModel, SluggedModel, \
    ModelWithImageSet, PopularityTrackedModel, TaggedModel, \
    CommentedModel, SearchableModel
from images.models import Image

class Donor(AuditedModel, SluggedModel, ModelWithImageSet, PopularityTrackedModel, SearchableModel, models.Model):
    """
    Donor model. An example of a donor would be "AusAID"
    """
    name = models.CharField(
        max_length=250)
    biography = models.TextField(
        "Biography",
        null=False,
        help_text="Short summary of the donor.")
    url = models.CharField(
        help_text="A URL for the donors website",
        max_length=250,
        blank=True,
        null=True)

    def slug_from_field(self):
        return self.name

    def imageset(self):
        """
        Override the abstract method. This does assume we've
        defined a ProgrammeImage model somewhere
        """
        return self.donorimage_set.all()
    
    def __unicode__(self):
        return "%s" % (self.name)
        
    def get_absolute_url(self):
        return '/about-us/donors'
        
    @models.permalink  
    def get_list_url(self):
        return (str(self.content_type()) + 's_' + str(self.content_type()) + 's', (), {})
    
    def content_type(self):
        """
        To help in templates.
        """
        return self._meta.module_name

    def search_result_title(self):
        return self.name

    def search_result_summary(self):
        return self.biography
        
class DonorImage(Image):
    donor = models.ForeignKey(Donor)
