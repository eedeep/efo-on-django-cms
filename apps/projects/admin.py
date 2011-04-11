from django.contrib import admin
from django.contrib import databrowse
from django.db.models import get_model

from modelmixins.admin import AuditedModelAdmin
from images.admin import ImageInline
from projects.forms import ProjectAdminModelForm, ProjectLocationAdminModelForm
    
from projects.models import *
from images.models import *

class ProjectLocationAdmin(admin.ModelAdmin):
    list_display = (
        'name',
    )
    
admin.site.register(get_model('projects', 'projectlocation'), ProjectLocationAdmin)
databrowse.site.register(ProjectLocation)

class ProjectImageInline(ImageInline):
    #exclude = ('feature', 'slide_show')
    model = get_model('projects', 'projectimage')
    
databrowse.site.register(ProjectImage)
    
class ProjectAdmin(AuditedModelAdmin):
    list_display = (
        'name',
        'created_meta',
        'modified_meta',
    )
    
    list_editable = (
        # 'is_published',
    )
    
    # filter_horizontal = ('project_categories', 'project_types')
    
    fieldsets = (
        (None, {
            'fields': (
                'name',
                'programme',
                'summary',
                'spiele',
            )
        }),
        ('Project Information', {
            'fields': (
                'beneficiaries',
                'location',
                'date_started',
                )
        }),
    )
    
    filter_horizontal = ('tags',)
    
    inlines = [
        ProjectImageInline,
    ]
    
    form = ProjectAdminModelForm

admin.site.register(get_model('projects', 'project'), ProjectAdmin)
databrowse.site.register(Project)
