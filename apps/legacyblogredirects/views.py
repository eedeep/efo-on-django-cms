from django.shortcuts import get_object_or_404
from django.shortcuts import render_to_response
from django.shortcuts import redirect
from django.template.context import RequestContext
import re
from zinnia.models import Entry

def legacy_blog_entry_redirect(request):

    entry = Entry.objects.get(slug=request.path.strip('/').lower())

    return redirect(entry.get_absolute_url(), permanent=True)
