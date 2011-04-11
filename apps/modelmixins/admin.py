import datetime

from django.contrib import admin
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import get_model
from django.shortcuts import _get_queryset

def update_audit_meta(request, obj, klass, change, save_object=True):
    """
    Base model 'admin' utility to auto update meta fields

        Assuming that the following fields are present
            created_by
            created
            modified_by
            modified
    """

    if not obj.id:
        obj.created_by = request.user
        obj.created = datetime.datetime.now()
    else:
        if change:
            obj.modified_by = request.user
            obj.modified = datetime.datetime.now()

    if save_object:
        obj.save()

class AuditedModelAdmin(admin.ModelAdmin):
    
    def created_meta(self, obj):
        return u'%s<br> by %s' % (
            obj.created.strftime('%d %b %Y %H:%M'), 
            obj.created_by)
    created_meta.allow_tags=True
    created_meta.short_description= 'created'
    
    def modified_meta(self, obj):
        if obj.modified:
            return u'%s<br> by %s' % (
                obj.modified.strftime('%d %b %Y %H:%M'), 
                obj.modified_by)
        else:
            return u''
    modified_meta.allow_tags=True
    modified_meta.short_description= 'modified'
    
    def save_model(self, request, obj, form, change):
        update_audit_meta(
            request, obj, self.model, change, True)
            
    class Media:
        css = { 
            'all': ['/site_media/static/admin_overrides/css/admin.css', ]
        }
        js = [
            '/site_media/static/admin/tinymce/jscripts/tiny_mce/tiny_mce.js', 
            '/site_media/static/admin/tinymce_setup/tinymce_setup.js',
            '/site_media/static/admin/filebrowser/js/TinyMCEAdmin.js',]
