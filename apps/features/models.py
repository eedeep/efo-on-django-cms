from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes import generic
from django.contrib.sites.managers import CurrentSiteManager
from django.contrib.sites.models import Site
from django.db.models import get_model
from django.core import urlresolvers

import datetime
        
FEATURE_AREA_CHOICES = (
    ('home', 'Home'),
    ('editors_choice', 'Editors Choice'),
)        
        
class SiteFeatureArea(models.Model):
    """
    A Site's Feature Area
    """
    site = models.ForeignKey(
        Site,
        help_text="Choose the site that this feature set should appear.",
        null=True)
    objects = models.Manager()
    site_objects = CurrentSiteManager('site')
        
    area = models.CharField(
        choices=FEATURE_AREA_CHOICES,
        default='home',
        max_length=50,
        verbose_name="Feature area")
        
    class Meta:
        unique_together = ('site', 'area')   
    
    def __unicode__(self):
        return u'%s (%s)' % (self.site.name, self.area)
        
class FeatureSet(models.Model):
    """
    A set of features set to show on a site feature area
    """
    site_feature_area = models.ForeignKey(
        SiteFeatureArea,
        null=True)
        
    def __unicode__(self):
        return u'%s' % (self.site_feature_area)

class Feature(models.Model):
    """
    A Feature
    
    Features appear in 'Feature' places, like the Home page.
    
    Features reference another object, such as an article,
    or an event, to feature on the given area.
    """
    
    feature_set = models.ForeignKey(
        FeatureSet,
        null=True)
        
    content_type = models.ForeignKey(
        ContentType,
        default='programme',
        limit_choices_to={ 'model__in': ['programme', 'project']}) # article for now.
    object_id = models.PositiveIntegerField(
        "Programme or project lookup")
    content_object = generic.GenericForeignKey(
        'content_type',
        'object_id')
    
    active = models.BooleanField()
    feature_summary = models.CharField(
        max_length=200,
        blank = False,
        null = False,
        help_text='A short summary for the feature')
    order = models.PositiveIntegerField(
        blank=True, 
        null=True)
    
    class Meta:
        ordering = ['order']
        
    def __unicode__(self):
        return u'%s' % self.content_object
    
    def content_object_change_url(self):
        """
        Provide a convenience shortcut to the featured object
        change_url.
        """
        url_name = 'admin:%s_%s_change' % (
            self.content_type.app_label, self.content_type.model)
        return urlresolvers.reverse(
            url_name, 
            args=(self.content_type.model_class().objects.get(pk=self.object_id).id,))
        
    def is_published(self):
        return self.content_type.model_class().objects.get(
            pk=self.object_id).is_published
        
    def feature_image(self):
        """
        Return the first image as the feature.
        """
        try:
            return self.feature_images()[0] 
        except IndexError:
            return None
            
    def feature_images(self):
        """
        Resolve and return the appropriate feature images.
        """
        return self.content_object.feature_images()

class FeatureSchedule(models.Model):
    """
    Feature or FeatureSet scheduling
    
    * Not yet in use.
    """
    
    # feature = models.ForeignKey(Feature)
    start_date_time = models.DateTimeField(default=datetime.datetime.now)
    end_date_time = models.DateTimeField(
        blank=True, 
        help_text="Continous if no end date/time is specified", 
        default=datetime.datetime.now)
        
    """
    Times should not overlap?
    If a schedule is continuous, should no further schedules be allowed?
    """
