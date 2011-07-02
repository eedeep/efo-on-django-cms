import ipdb
from django import forms
from django.db.models import get_model
from django.contrib.admin.widgets import ForeignKeyRawIdWidget
from django.db.models.fields.related import ManyToOneRel
from widgets import ContentTypeSelect

from programmes.models import Programme
from features.models import Feature

class FeatureAdminModelForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
            super(FeatureAdminModelForm, self).__init__(*args, **kwargs)
            try:
                model = self.instance.content_type.model_class()
                model_key = model._meta.pk.name
            except:
                model = Programme
                model_key = 'id'

            self.fields['object_id'].widget = ForeignKeyRawIdWidget(rel=ManyToOneRel(model, model_key))
            self.fields['content_type'].widget.widget = ContentTypeSelect('lookup_id_object_id', 
                            self.fields['content_type'].widget.widget.attrs, 
                            self.fields['content_type'].widget.widget.choices)

    class Meta:
        model = Feature
