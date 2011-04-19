from django import forms
from django.db.models import get_model

class ProjectAdminModelForm(forms.ModelForm):
    
    class Meta:
        model = get_model('projects', 'project')
        widgets = {
            'spiele': forms.Textarea(
                attrs={ 'class': 'mceEditor', }),
        }

class ProjectLocationAdminModelForm(forms.ModelForm):
    class Meta:
        model = get_model('projects', 'projectlocation')
