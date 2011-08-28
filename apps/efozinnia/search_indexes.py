import datetime
from haystack.indexes import *
from haystack import site
from zinnia.models import Entry

class EntryIndex(SearchIndex):
    text = CharField(document=True, use_template=True)

    def index_queryset(self):
        """Used when the entire index for model is updated."""
        return Entry.objects.all()

site.register(Entry, EntryIndex)
