import os

from django.contrib.auth.models import User
from django.contrib.sites.models import Site
from django.core.exceptions import ObjectDoesNotExist
from django.db import models
from django.db.models.signals import pre_save, post_save
from django.utils.translation import ugettext_lazy as _

from filebrowser.fields import FileBrowseField
from emailconfirmation.models import EmailAddress

from settings import FEATURED_COUNTRIES

from idios.models import ProfileBase
from idios.utils import get_profile_model

User._meta.ordering = ['last_name', 'first_name']

class Profile(ProfileBase):
    """
    Architecture Now Member/Contributor profile
    """
    
    is_contributor = models.BooleanField(
        "AM Contributor",
        blank=True,
        default=False,
        help_text="AM manages the profile information.  Contributors can only change the password and email addresses via the public site",
    )
    
    # Location
    location = models.CharField(
        blank=True,
        max_length=255
    )
    
    # @@@ Deprecate and defer to a possible 'LocationField' for now, a CharField abov
    # street = models.CharField(max_length=200, blank=True)
    #     city = models.CharField(max_length=200, blank=True)
    #     suburb = models.CharField(max_length=200, blank=True)
    #     country = models.CharField(max_length=200,
    #         blank=True, choices=FEATURED_COUNTRIES)
    #     state = models.CharField(max_length=200, blank=True)
    #     post_code = models.CharField(max_length=10, blank=True)
    # @@@ end
    
    website = models.URLField(
        blank=True,
        max_length=200)
    
    # Profile
    profession = models.CharField(
        blank=True, 
        max_length=200)
    biography = models.TextField(
        "Bio", 
        blank=True)
    
    # Avatar
    avatar = FileBrowseField(
        "Avatar",
        blank=True,
        directory="avatars/", 
        max_length=250,
        null=True)

    site = models.ForeignKey(
        Site,
        blank=True,
        null=True,
        verbose_name="Member of")
        
    def __unicode__(self):
        return u'%s' % self.display_name()
        
    def display_name(self):
        """
        Resolve the displayable name for the user
        """
        if self.user.first_name and self.user.last_name:
            return u'%s %s' % (self.user.first_name, self.user.last_name)
        elif self.user.first_name:
                    return u'%s' % self.user.first_name
        else:
            return u'%s' % self.user.username
            
    def has_verified_email(self):
        try:
            email_address = EmailAddress.objects.get(
                verified=True,
                user=self.user)
        except ObjectDoesNotExist:
            return False
        else:
            return True
            
    def has_feature_image(self):
        if self.avatar:
            return True
        else:
            return False
        
    def can_comment(self):
        """
        A Set of conditions determining whether we allow a user to comment
        """
        return self.has_verified_email()
    
    @models.permalink
    def get_absolute_url(self):
        """
        Override the default Pinax version of the url
        """
        return ('profile_view', (), {
            'username': self.user.username,
        })
        
    @models.permalink  
    def get_list_url(self):
        return ('profiles_list', (), {})
        
    def content_type(self):
        return u'profile'
