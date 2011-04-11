import datetime
import re

from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from django import template
from django.utils.safestring import mark_safe
from django.utils.translation import ugettext_lazy as _
from django.template.context import Context

from empcom.util.regex import in_admin_regex
from models import ScheduledSnippetPtr

class ScheduledSnippetPlugin(CMSPluginBase):
    """
    A plugin which allows scheduling of snippets of HTML/text in the django-cms
    Most of this processing has to do with displaying the snippet in admin preview mode
    """

    model = ScheduledSnippetPtr
    name = _("Scheduled Snippet")
    render_template = "cms/plugins/snippet.html"
    text_enabled = True

    def render(self, context, instance, placeholder):
        request = context['request']
        isStaff = request.user.is_staff
        inAdminArea = re.match(in_admin_regex, request.path)
        inPreviewMode = request.GET.__contains__('preview')
        withinDates = instance.snippet.startDateTime < datetime.datetime.now() < instance.snippet.endDateTime

        if (isStaff and (inPreviewMode or inAdminArea)) or withinDates:
            try:
                t = template.Template(instance.snippet.html)
                content = t.render(Context(context))

                pluginTemplateName = self.determineTemplate(isStaff, inPreviewMode, inAdminArea, withinDates)
                pluginTemplate = template.loader.get_template(pluginTemplateName)
                pluginContent = pluginTemplate.render(Context({
                    'content' : mark_safe(content),
                    'imageUrl' : self.icon_src(instance),
                    'snippetName' : instance.snippet.name,
                    'startDate' : instance.snippet.startDateTime,
                    'endDate' : instance.snippet.endDateTime,
                    }))
            except Exception, e:
                content = str(e)
            context.update({
                'content': pluginContent,
                'placeholder': placeholder,
                'object': instance,
            })

        return context

    def icon_src(self, instance):
        return u"/media/media/images/plugins/scheduledSnippet.png"

    def determineTemplate(self, isStaff, isPreview, inAdminArea, withinDates):
        normalTemplate = 'cms/plugins/scheduledSnippet.html'
        adminTemplate = 'cms/plugins/previewScheduledSnippet.html'

        if isStaff and (isPreview or inAdminArea) and not withinDates:
            return adminTemplate
        return normalTemplate

plugin_pool.register_plugin(ScheduledSnippetPlugin)
