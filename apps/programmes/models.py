import ipdb
import datetime

from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.comments.models import Comment
from popularity.models import ViewTracker

from features.models import Feature, FeatureSet
from modelmixins.models import AuditedModel, SluggedModel, \
    ModelWithImageSet, PopularityTrackedModel, TaggedModel, \
    CommentedModel
from images.models import Image

class Programme(AuditedModel, SluggedModel, ModelWithImageSet, PopularityTrackedModel, TaggedModel, CommentedModel, models.Model):
    """
    Programme model. An example of a programme would be "health" or "education".
    """
    name = models.CharField(
        max_length=250)
    summary = models.TextField(
        "Summary",
        null=False,
        help_text="Short summary of the programme.")
    spiele = models.TextField(
        "Spiele",
        null=False)
    feature_sets = models.ManyToManyField(
        FeatureSet,
        blank=True,
        help_text="Feature this content on the selected sites and feature areas.  Note, the content must be published on the corresponding site to take effect.",
        null=True)

    def slug_from_field(self):
        return self.name

    def imageset(self):
        """
        Override the abstract method. This does assume we've
        defined a ProgrammeImage model somewhere
        """
        return self.programmeimage_set.all()

    def __unicode__(self):
        return "%s" % (self.name)

    @models.permalink
    def get_absolute_url(self):
        return (str(self.content_type()) + '_view', (), {
            'slug': self.slug,
        })

    @models.permalink
    def get_list_url(self):
        return (str(self.content_type()) + 's_' + str(self.content_type()) + 's', (), {})

    def content_type(self):
        """
        To help in templates.
        """
        return self.__class__.__name__.lower()


class ProgrammeImage(Image):
    programme = models.ForeignKey(Programme)
