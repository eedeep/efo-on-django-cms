import datetime
from haystack.indexes import *
from haystack import site
from donors.models import Donor

class DonorIndex(SearchIndex):
    text = CharField(document=True, use_template=True)

    def index_queryset(self):
        """Used when the entire index for model is updated."""
        return Donor.objects.all()

site.register(Donor, DonorIndex)
