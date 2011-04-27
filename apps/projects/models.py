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
from programmes.models import Programme

class ProjectLocation(models.Model):
    name = models.CharField(
        max_length=250,
        null=False)

class Project(AuditedModel, SluggedModel, ModelWithImageSet, PopularityTrackedModel, TaggedModel, CommentedModel, models.Model):
    """
    Project model. An example of a project would be "kamakwie secondary school" or "Kailahun hospital".
    """
    name = models.CharField(
        max_length=250)
    programme = models.ForeignKey(
        Programme,
        null=False,
        help_text="The programme area that this project is most relevant to.")
    summary = models.TextField(
        "Summary",
        null=False,
        help_text="Short summary of the project.")
    spiele= models.TextField(
        "Spiele",
        null=False)
    feature_sets = models.ManyToManyField(
        FeatureSet,
        blank=True,
        help_text="Feature this content on the selected sites and feature areas.  Note, the content must be published on the corresponding site to take effect.",
        null=True)
    beneficiaries = models.PositiveIntegerField(
            help_text="How many people benefited from the project?",
            null=False)
    location = models.ForeignKey(ProjectLocation)
    date_started = models.DateField(
        null=False)

    def slug_from_field(self):
        return self.name

    def imageset(self):
        """
        Override the abstract method. This does assume we've
        defined a ProgrammeImage model somewhere
        """
        return self.projectimage_set.all()
    
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
        return self._meta.module_name
        
            
class ProjectImage(Image):
    project = models.ForeignKey(Project)
