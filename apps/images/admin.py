from django.contrib import admin
from django.db.models import get_model

from images.forms import ImageAdminModelForm

class ImageInline(admin.StackedInline):
    extra = 0
    form = ImageAdminModelForm
    sortable_field_name = "order"
    fieldsets = (
        (None, {
            'fields': (
                'image',
                'caption',
                'photographer',
                'slide_show',
                'feature',
            )
        }),
    )

class ImageAdmin(admin.ModelAdmin):
    pass

admin.site.register(get_model('images', 'image'), ImageAdmin)
