import datetime
from haystack.indexes import *
from haystack import site
from programmes.models import Programme

class ProgrammeIndex(SearchIndex):
    text = CharField(document=True, use_template=True)

    def index_queryset(self):
        """Used when the entire index for model is updated."""
        return Programme.objects.all()

site.register(Programme, ProgrammeIndex)
