from models import ScheduledSnippet
from django.contrib import admin

class ScheduledSnippetAdmin(admin.ModelAdmin):
    pass

admin.site.register(ScheduledSnippet, ScheduledSnippetAdmin)
