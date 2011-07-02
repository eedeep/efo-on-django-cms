import datetime

from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.comments.models import Comment
from popularity.models import ViewTracker

from features.models import Feature, FeatureSet
from modelmixins.models import AuditedModel, SluggedModel, \
    ModelWithImageSet, PopularityTrackedModel, TaggedModel, \
    CommentedModel, SearchableModel
from images.models import Image
from programmes.models import Programme

class ProjectLocation(models.Model):
    name = models.CharField(
        max_length=250,
        null=False)

    def __unicode__(self):
        return "%s" % (self.name)

class Project(AuditedModel, SluggedModel, ModelWithImageSet, PopularityTrackedModel, TaggedModel, CommentedModel, SearchableModel,models.Model):
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
    donors = models.CharField(
        help_text="The donor or donors that contributed to the project ",
        max_length=250,
        blank=True,
        null=True)
    location = models.ForeignKey(ProjectLocation)
    system_size= models.CharField(
        help_text="The system size in watts",
        max_length=250,
        blank=True,
        null=True)
    direct_beneficiaries = models.PositiveIntegerField(
        help_text="How many people directly benefited from the project?",
        blank=True,
        null=True)
    indirect_beneficiaries = models.PositiveIntegerField(
        help_text="How many people indirectly benefited from the project?",
        blank=True,
        null=True)
    date_started = models.DateField(
        help_text="When did the project start?",
        blank=True,
        null=True)
    date_finished = models.DateField(
        help_text="When was the project completed?",
        blank=True,
        null=True)

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

    def search_result_title(self):
        return self.name

    def search_result_summary(self):
        return self.spiele
        
            
class ProjectImage(Image):
    project = models.ForeignKey(Project)
