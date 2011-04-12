from django.contrib import admin
from django.contrib.contenttypes import generic
from django.db.models import get_model

class FeatureScheduleInline(admin.TabularInline):
    model = get_model('features', 'featureschedule')
    extra = 1

# class FeatureAreaAdmin(admin.ModelAdmin):
#     pass
# admin.site.register(get_model('features', 'featurearea'), FeatureAreaAdmin)

class SiteFeatureAreaAdmin(admin.ModelAdmin):
    pass
admin.site.register(get_model('features', 'sitefeaturearea'), SiteFeatureAreaAdmin)

class FeatureAdmin(admin.ModelAdmin):
    list_display = (
        'content_object',
        'content_object_change_url',
        'content_type',
        'active',
        'ordering',
        'is_published',)
    
    list_filter = ()
    
    list_editable = (
       'active',
       'ordering',)
    
    def content_object_change_url(self, obj):
        
        return '<a href="%s">%s</a> &rarr;'  % (
            obj.content_object_change_url(),
            obj.content_object)
    content_object_change_url.allow_tags=True
    content_object_change_url.short_description= 'Content title'
    
    list_display_links = (
        # 'content_object_change_url',
    )
    
class FeatureInline(admin.StackedInline):
    model = get_model('features', 'feature')
    extra = 0
    sortable_field_name = "order"
    
class FeatureSetAdmin(admin.ModelAdmin):
    list_display = (
        'site_feature_area',)
    
    list_filter = ()
    
    inlines = [
        FeatureInline,]
    
admin.site.register(get_model('features', 'featureset'), FeatureSetAdmin)

class ObjectFeatureInline(generic.GenericStackedInline):
    """
    A Generic Inline for editing features inline with other app objects
    """
    model = get_model('features', 'feature')
    extra = 1
    exclude = ('order', 'active')