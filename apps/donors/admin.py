from django.contrib import admin
from django.contrib import databrowse
from django.db.models import get_model

from modelmixins.admin import AuditedModelAdmin
from images.admin import ImageInline
from donors.forms import DonorAdminModelForm
    
from donors.models import *
from images.models import *

class DonorImageInline(ImageInline):
    #exclude = ('feature', 'slide_show')
    model = get_model('donors', 'donorimage')
    template = 'patches/tabular.html'
    
#databrowse.site.register(ProjectImage)
    
class DonorAdmin(AuditedModelAdmin):
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
                'biography',
                'url',
            )
        }),
    )
    
    inlines = [
        DonorImageInline,
    ]
    
    form = DonorAdminModelForm

admin.site.register(get_model('donors', 'donor'), DonorAdmin)
#databrowse.site.register(Project)
