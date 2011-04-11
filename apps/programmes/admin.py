from django.contrib import admin
from django.contrib import databrowse
from django.db.models import get_model

from modelmixins.admin import AuditedModelAdmin
from images.admin import ImageInline
from programmes.forms import ProgrammeAdminModelForm
    
from programmes.models import *
from images.models import *

class ProgrammeImageInline(ImageInline):
    model = get_model('programmes', 'programmeimage')
    
#databrowse.site.register(ProgrammeImage)
    
"""
TODO: probably need some kind of assertion type mechanism here to 
ensure that if the admin class is for a model that mixes in
classes from modelmixins then the admin class inherits from
the correct modelmixin Admin base classes.
"""
class ProgrammeAdmin(AuditedModelAdmin):
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
                'summary',
                'spiele',
            )
        }),
    )
    
    filter_horizontal = ('tags',)
    
    inlines = [
        ProgrammeImageInline,
    ]
    
    form = ProgrammeAdminModelForm

admin.site.register(get_model('programmes', 'programme'), ProgrammeAdmin)
databrowse.site.register(Programme)
