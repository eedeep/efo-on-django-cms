import ipdb
from django.db import models, IntegrityError, transaction
from django.template.defaultfilters import slugify
from exceptions import NotImplementedError 
from django.contrib.comments.models import Comment
from django.contrib.auth.models import User
from popularity.models import ViewTracker
from taggit.models import Tag

class SluggedModel(models.Model):
    """
    This assumes the inheriting class will have instaces that use a 'name' field, from 
    which the slug will be generated.
    """
    slug = models.SlugField(
        blank=False,
        editable=False,
        max_length=250,
        unique=True)

    def slug_from_field(self):
       """Force the inheritor to implement. This is one way of defining an abstract method."""
       raise NotImplementedError 

    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        self.slug = slugify(self.slug_from_field())
        i = 0
        while True:
            try:
                savepoint = transaction.savepoint()
                result = super(SluggedModel, self).save(*args, **kwargs)
                transaction.savepoint_commit(savepoint)
                return result
            except IntegrityError:
                transaction.savepoint_rollback(savepoint)
                i += 1
                self.slug = '%s-%d' % (self.slug_from_field(), i)

class AuditedModel(models.Model):
    created = models.DateTimeField( 
        auto_now_add=True)
    modified = models.DateTimeField(
        auto_now=True)
    created_by = models.ForeignKey(
        User,
        blank=True,
        editable=False,
        related_name="%(app_label)s_%(class)s_created_by",
        null=True)
    modified_by = models.ForeignKey(
        User,
        blank=True,
        editable=False,
        related_name="%(app_label)s_%(class)s_modified_by",
        null=True)

    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
#        if not self.pk:
#            created_by = request.user
#        else:
#            modified_by = request.user

        return super(AuditedModel, self).save(*args, **kwargs)


class ModelWithImageSet(models.Model):

    class Meta:
        abstract = True

    def feature_image(self):
        try:
            # Return the first image as feature
            return self.feature_images()[0]
        except:
            """
            IndexError or others.
            """
            return None

    def has_feature_image(self):
        if len(self.feature_images())>0 and self.feature_images()[0].image:
            return True
        else:
            return False

    def has_slideshow(self):
        """
        Return true if the article has at least 2 slideshow images
        """
        return True if len(self.slideshow_images()) >= 2 else False 

    def feature_images(self):
        """
        Resolve and return the appropriate feature images
        """
        return self.imageset().filter(feature=True)

    def slideshow_images(self):
        """
        Return slideshow images.
        """
        return self.imageset().all()

    def imageset(self):
        raise NotImplementedException

    def summary_image(self):
        summary_images = self.imageset().filter(summary=True)
        if len(summary_images) >= 1:
            return summary_images[0]
        elif self.has_feature_image():
            return self.feature_image()
        else:
            return None


class CommentedModel(models.Model):

    class Meta:
        abstract = True

    def comments(self):
        """
        Get the comments for this object, if any.
        """
        comments = []
        all_comments = Comment.objects.get_query_set()
        for comment in all_comments:
            if comment.is_removed == False and comment.content_object == self:
                comments.append(comment)

        return comments

    def comments_count(self):
        try:
            return u'%s' % len(self.comments())
        except:
            None


class PopularityTrackedModel(models.Model): 

    class Meta:
        abstract = True

    def view_count(self):
        """
        From django-popularity, get the view count for the object.
        This is used to sort objects in a list view.
        """
        return ViewTracker.get_views_for(self)

    def popularity(self):
        """
        Relative popularity calculated as views/age. Depends on AuditedModel
        also being mixed in.
        """
        try:
            return self.view_count() / (datetime.datetime.now() - self.created).days
        except:
            None


class TaggedModel(models.Model):

    class Meta:
        abstract = True

    tags = models.ManyToManyField(
        Tag,
        blank=True,
        null=True,
        related_name="%(app_label)s_%(class)s_tags")


class SearchableModel(models.Model):

    class Meta:
        abstract = True

    def search_result_title(self):
       """Force the inheritor to implement. This is one way of defining an abstract method."""
       raise NotImplementedError 

    def search_result_summary(self, data):
       """Force the inheritor to implement. This is one way of defining an abstract method."""
       raise NotImplementedError 
